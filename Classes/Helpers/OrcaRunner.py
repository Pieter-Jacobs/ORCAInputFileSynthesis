import os
import subprocess
import glob
import shutil
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from collections import namedtuple
import psutil
import time


class ORCARunner():
    """Static class to run an ORCA input file, and handle its corresponding output."""
    def kill_processes_by_file(file_path):
        # Get a list of all running processes
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if 'orca' in proc.name().lower() or 'autoci' in proc.name().lower():
                try:
                    print(f"Terminating {proc.name()}")
                    proc.kill()
                    time.sleep(15)

                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                    print(e)

    def run_orca(data_folder,  input_file_name, main_output_folder, orca_executable):
        """Function that runs an orca input file and moves the output to a dedicated folder within the output folder."""
        specific_output_folder = os.path.join(
            main_output_folder, input_file_name)
        if os.path.exists(specific_output_folder):
            shutil.rmtree(specific_output_folder)
        os.makedirs(specific_output_folder)

        input_file_path = f'{data_folder}{os.sep}{input_file_name}'

        # Construct the output file paths
        output_file_stdout = os.path.join(
            specific_output_folder, f'{input_file_name}.txt')
        output_file_stderr = os.path.join(
            specific_output_folder, 'error.txt')
        # Construct the command to run Orca with the input file
        # command = [orca_executable, input_file_path,
        #            f'-l {output_file_stdout}']
        command = [orca_executable, input_file_path]
        # Run the ORCA process and redirect output
        try:
            with open(output_file_stdout, 'w') as output_file, open(output_file_stderr, 'w') as error_file:
                completed_process = subprocess.run(
                    command, stdout=output_file, stderr=error_file, text=True, timeout=5, encoding='utf-8')
        except Exception as e:
            print(e)
            DummyProcess = namedtuple("completed_process", [
                                      "returncode", "stderr"],)
            completed_process = DummyProcess(1, "Timeout")
        try: 
            ORCARunner.rename_orca_output(
                completed_process, output_file_stdout, output_file_stderr)
        except:
            pass
        ORCARunner.move_output_files(data_folder, specific_output_folder)

        return completed_process.returncode

    def remove_unrunnable_orca_files(data_folder_read, output_folder, data_folder_write=None):
        """
        Tries to run an ORCA file, if an error is raised, it gets deleted.
        If data_folder_write is defined, working files are written from data_folder_read to data_folder_write.

        Args:
            data_folder_read (str): Path to the folder containing input ORCA files.
            output_folder (str): Path to the folder where output files will be saved.
            data_folder_write (str, optional): Path to the folder where working files will be written. Defaults to None.
        """
        # Get a list of input files in the defined folder
        for file_name in os.listdir(data_folder_read):
            file_path = os.path.join(data_folder_read, file_name)
            # Try to run the file
            return_code = ORCARunner.run_orca(
                data_folder_read, file_name, output_folder)
            # If the file does not work and we are working with one data folder, remove it from that folder
            if return_code != 0 and data_folder_write is None:
                os.remove(file_path)
            # If the file works, we don't remove it and if working with two data folders we write it to the write folder
            elif return_code == 0 and data_folder_write is not None:
                input_file_code = ORCAInputFileManipulator.read_file(file_path)
                ORCAInputFileManipulator.write_file(
                    os.path.join(data_folder_write), input_file_code)

    def rename_orca_output(completed_process, output_file_stdout, output_file_stderr):
        """Writes the output of the orca file. If there was an error, this is made to be seen in the filename."""
        if completed_process.returncode != 0:
            error = ORCAInputFileManipulator.read_file(output_file_stderr)
            new_path = output_file_stdout.removesuffix(
                '.txt') + '_error' + '.txt'
            if hasattr(completed_process, 'stderr') and completed_process.stderr == 'Timeout':
                print('Timed out, killing child processes...')
                ORCARunner.kill_processes_by_file(output_file_stdout)

            os.rename(output_file_stdout, new_path)

            # If there was an error, create an error file with the stderr content
            with open(new_path, "a", encoding='utf-8') as output_file:
                output_file.write(
                    f"Error during ORCA execution:\n\n{error}")
        else:
            new_path = output_file_stdout.removesuffix(
                '.txt') + '_completed' + '.txt'
            os.rename(output_file_stdout, new_path)
            print("Orca job completed successfully.")

    def move_output_files(old_folder, new_folder):
        """Moves output (non .inp files) from one folder to another"""
        for file_path in glob.glob(os.path.join(old_folder, '*')):
            if not file_path.endswith('.inp') or (
                file_path.endswith('.inp') and "Compound" in file_path) or (
                    file_path.endswith('rel.inp')
            ) or file_path.endswith('loc.inp') or (
                    file_path.endswith('scfgrad.inp')) or (
                    file_path.endswith('scfhess.inp')) or (
                        file_path.endswith('cipsi.inp')
                    ):
                # Get the filename
                file_name = os.path.basename(file_path)
                # Move the file to the destination folder
                shutil.move(file_path, os.path.join(new_folder, file_name))
