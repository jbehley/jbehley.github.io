"""
Given a list of indices seperate directories for training data and validation data is generated.
This reproduces the training set and validation set used in [1].

Contact: If you have a question relating to the evaluation you can contact me via behley@iai.uni-bonn.de.

[1] J. Behley, V. Steinhage, A.B. Cremers. Laser-based Segment Classification Using a Mixture of Bag-of-Words, 
Proc. of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2013.

"""

import os
import sys
import numpy
import shutil

def checkdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print dirname + " created."

if __name__ == "__main__":
    # change filenames to appropriate locations.
    validx_filename = "validation_idxes.txt" # indices of the original training images used as validation set (download from website).
    input_dirname = "../kitti-detection/training-original/" # KITTI detection files from website.
    trainout_dirname = "../kitti-detection/training/" # output directory of the new training set
    valout_dirname = "../kitti-detection/validation/" # output directory of the extracted validation set
    
    valin = open(validx_filename)
    validx = [int(line) for line in valin]
    valin.close()
    
    print "first and last 10 entries from idx-file: " + ", ".join([str(val) for val in validx[0:10]]) + ", ..., " + ", ".join([str(val) for val in validx[-10:]])
    
    sub_dirnames = [os.path.normcase(f) for f in os.listdir(input_dirname)];
    print "sub_dirnames = ", sub_dirnames
    #sub_dirnames = ['calib']
    
    checkdir(trainout_dirname)
    checkdir(valout_dirname)
        
    for sub_dirname in sub_dirnames:
        # for every sub directory...
        csub_dirname = os.path.join(input_dirname, sub_dirname)
        if os.path.isdir(csub_dirname):
            # we generate a corresponding output directory
            trainsub_dirname = os.path.join(trainout_dirname, sub_dirname)
            valsub_dirname = os.path.join(valout_dirname, sub_dirname)

            checkdir(trainsub_dirname)
            checkdir(valsub_dirname)
            
            subfiles = os.listdir(csub_dirname)
            # now take every file, and copy it to the corresponding directory.
            for file in subfiles:
                src = os.path.join(csub_dirname, file)
                
                # determine the destination directory.
                (basename, ext) = os.path.splitext(file)
                
                dst = os.path.join(trainsub_dirname, file)                
                if int(basename) in validx:
                    dst = os.path.join(valsub_dirname, file)
                shutil.copy(src, dst)
    
    
