"""
xtb.py - interface to mopac program
Copyright (C) 2016 by Surajit Nandi, Anoop Ayyappan, and Mark P. Waller
Indian Institute of Technology Kharagpur, India and Westfaelische Wilhelms
Universitaet Muenster, Germany

This file is part of the PyAR project.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""
import os
import subprocess as subp

import numpy as np

import interface.babel


class Xtb(object):
    def __init__(self, molecule, charge, multiplicity, scftype):
        self.job_name = molecule.name
        self.start_xyz_file = 'trial_' + self.job_name + '.xyz'
        self.cmd = "xtb {} -opt".format(self.start_xyz_file)
        if charge != 0:
            self.cmd = "{} -chrg {}".format(self.cmd, charge)
        if multiplicity != 1:
            self.cmd = "{} -uhf {}".format(self.cmd, multiplicity)
        if multiplicity == 1 and scftype is not 'rhf':
            self.cmd = "{} -{}".format(self.cmd, scftype)
        self.atoms_list = molecule.atoms_list
        if not os.path.isfile(self.start_xyz_file):
            interface.babel.write_xyz(self.atoms_list, molecule.coordinates, self.start_xyz_file, job_name=self.job_name)
        self.result_xyz_file = 'result_' + self.job_name + '.xyz'
        self.trajectory_xyz_file = 'traj_' + self.job_name + '.xyz'

    def optimize(self, gamma=None):
        """
        """
        out = subp.check_output(self.cmd.split())
        if os.path.isfile('.xtboptok'):
            interface.babel.write_xyz(self.atoms_list, self.optimized_coordinates, self.result_xyz_file,
                                      job_name=self.job_name,
                                      energy=self.energy)
            os.rename('xtbopt.log', self.trajectory_xyz_file)
            os.remove('.xtboptok')
            return True
        elif os.path.isfile('.sccnotconverged'):
            print('SCF Convergence failure in {} run in {}'.format(self.start_xyz_file, os.getcwd()))
        else:
            print('Something went wrong with {} run in {}'.format(self.start_xyz_file, os.getcwd()))
            return False

    @property
    def optimized_coordinates(self):
        """"""
        return np.loadtxt('xtbopt.xyz', dtype=float, skiprows=2, usecols=(1, 2, 3))

    @property
    def energy(self):
        with open('energy') as fp:
            return float(fp.readlines()[-2].split()[1])


def main():
    pass


if __name__ == "__main__":
    main()
