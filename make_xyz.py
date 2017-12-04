# coding: utf-8

import atomic_data as data
import math

def make_element():
    for i, element in enumerate(data.chemical_symbols[1:87]):
        atomic_number = i+1
        input_xyz_file = element+'.xyz'
        covalent_radius = data.covalent_radii[atomic_number]
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(1)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0 ))

def make_dimers():
    for i, element in enumerate(data.chemical_symbols[1:87]):
        atomic_number = i+1
        input_xyz_file = element+'2.xyz'
        covalent_radius = data.covalent_radii[atomic_number]
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(2)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1*covalent_radius, 0.0, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +1*covalent_radius, 0.0, 0.0))

def make_dimers():
    for i, element in enumerate(data.chemical_symbols[1:87]):
        atomic_number = i+1
        input_xyz_file = element+'2.xyz'
        covalent_radius = data.covalent_radii[atomic_number]
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(2)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1*covalent_radius, 0.0, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +1*covalent_radius, 0.0, 0.0))

def make_trimers():
    for i, element in enumerate(data.chemical_symbols[1:87]):
        atomic_number = i+1
        covalent_radius = data.covalent_radii[atomic_number]
        input_xyz_file = element+'3_linear.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(3)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -2 * covalent_radius, 0.0, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +2 * covalent_radius, 0.0, 0.0))
        input_xyz_file = element+'3_triangular.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(3)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1 * covalent_radius, 0.0, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, covalent_radius*3.0**0.5, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +1 * covalent_radius, 0.0, 0.0))
        input_xyz_file = element+'3_bent.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(3)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -2 * covalent_radius, 0.0, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, math.cos(math.radians(30)) * 2* covalent_radius, math.sin(math.radians(30)) * 2 * covalent_radius, 0.0))

def make_tetramers():
    for i, element in enumerate(data.chemical_symbols[1:87]):
        atomic_number = i+1
        covalent_radius = data.covalent_radii[atomic_number]
	cr=covalent_radius
        input_xyz_file = element+'4_linear.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -3.0 * covalent_radius, 0.0, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1.0*covalent_radius, 0.0, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +1.0 * covalent_radius, 0.0, 0.0))
	    fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +3.0 * covalent_radius, 0.0, 0.0))
        input_xyz_file = element+'4_square.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1 * cr, -1*cr, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 1*cr,- 1*cr, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 1*cr ,1*cr, 0.0))
	    fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1*cr ,1*cr, 0.0))
        input_xyz_file = element+'4_planer_cis.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0))
	    x2=2*cr*math.cos(math.pi/4)
	    y2=2*cr*math.sin(math.pi/4)
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x2, y2, 0.0 ))
	    x3=x2+2*cr
	    y3=y2+0
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x3,y3,0.0))
	    x4=x3+2*cr*math.cos(math.pi/4)
            y4=y3-2*cr*math.sin(math.pi/4)
	    fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x4,y4,0.0))
        input_xyz_file = element+'4_planer_trans.xyz'
	with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0))
            x2=2*cr*math.cos(math.pi/4)
            y2=2*cr*math.sin(math.pi/4)
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x2, y2, 0.0 ))
            x3=x2+2*cr
            y3=y2+0
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x3,y3,0.0))
            x4=x3+2*cr*math.cos(math.pi/4)
            y4=y3+2*cr*math.sin(math.pi/4)
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x4,y4,0.0))

	input_xyz_file = element+'4_planer_trigonal.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, 0.0))
            x2=2*cr
            y2=0
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x2, y2, 0.0 ))
            x3=2*cr*math.cos(2*math.pi/3)
            y3=2*cr*math.sin(2*math.pi/3)
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x3,y3,0.0))
            x4=2*cr*math.cos(-2*math.pi/3)
            y4=2*cr*math.sin(-2*math.pi/3)
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x4,y4,0.0))

	input_xyz_file = element+'4_planer_spoon.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
	    x1=2*cr*(1/math.sqrt(3)) + 2*cr
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x1, 0.0, 0.0))
            x2=2*cr*(1/math.sqrt(3))
            y2=0
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x2, y2, 0.0 ))
            x3=2*cr*math.cos(2*math.pi/3)*(1/math.sqrt(3))
            y3=2*cr*math.sin(2*math.pi/3)*(1/math.sqrt(3))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x3,y3,0.0))
            x4=2*cr*math.cos(-2*math.pi/3)*(1/math.sqrt(3))
            y4=2*cr*math.sin(-2*math.pi/3)*(1/math.sqrt(3))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x4,y4,0.0))

        input_xyz_file = element+'4_tetrahedral.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
            z1=math.sqrt(8/3)*cr
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, 0.0, z1))
            x2=2*cr*(1/math.sqrt(3))
            y2=0
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, x2, y2, 0.0 ))
            x3=2*cr*math.cos(2*math.pi/3)*(1/math.sqrt(3))
            y3=2*cr*math.sin(2*math.pi/3)*(1/math.sqrt(3))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x3,y3,0.0))
            x4=2*cr*math.cos(-2*math.pi/3)*(1/math.sqrt(3))
            y4=2*cr*math.sin(-2*math.pi/3)*(1/math.sqrt(3))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element,x4,y4,0.0))
	input_xyz_file = element+'4_bitriangle.xyz'
        with open(input_xyz_file, 'w') as fw:
            fw.write(str(4)+'\n')
            fw.write(data.atomic_names[atomic_number]+'\n')
	    fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, -1 * covalent_radius, 0.0, 0.0))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, covalent_radius*3.0**0.5, 0.0 ))
            fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, +1 * covalent_radius, 0.0, 0.0))
	    fw.write("{:2s} {:13.7f} {:13.7f} {:13.7f}\n".format(element, 0.0, -covalent_radius*3.0**0.5, 0.0 ))


def main():
    make_tetramers()

if __name__ == '__main__':
    main()
