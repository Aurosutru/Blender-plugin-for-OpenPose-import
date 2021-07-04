# OpenPose to Blender Action Plugin

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Preliminary Setup

# Select a screen space
    # Store screen space mode; OrigSSMode
    # Store screen space height; OrigSSHgt
    # Store screen space width; OrigSSWid
    # Store camera position, orientation and F-Stop properties if available
    # Convert to 3D full screen space area
    # Store screen space height; SSHgt
    # Store screen space width; SSWid

# Create OPose Mocap tab in Sidebar Region

# User Inputs

# Action Name; ActionName
	# If name is taken or illegal, ask for new name
# Select Target Armature (from dropdown list)
# Select Blender Camera (from dropdown list)
    # Create camera if necessary
# Select OpenPose file
    # Read number of frames and bones; OPFrames, Bones
    # Details at 
    # If error notify user to select another file
# Input Video Height (pixels); VidHgt
# Input Video Width (pixels); VidWid
# Camera to Character Distance (meters); CamToCharDist
# Camera Height (meters); CamHgt
# Camera Angle from Front View (+/- deg); CamAng
    #Limit CamAng to +/- 90 degrees
# Camera Lens Focal Length (mm); CamFocalLength
# Print "In Camera View Check That Target Character Matches Video Character"
# CREATE ACTION button
# Progress Bar

Check this section
# ScaleX=VidHgt/SSHgt
# ScaleY=VidWid/SSHWid
# If ScaleX<ScaleY then Scale=ScaleX
    else Scale=ScaleY
    
# OpenPose joint sequences
    # Note: All OpenPose JSON output files have data for body joints.  Availability of face and hand data
    # depends on the OpenPose output file having the --face and --hand flags enabled during creation.
    # For details see: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/02_output.md
    # Sequence for body joints : 0 through 24 for the standard Body_25
    # Sequence for face joints: 0 through 69
    # Sequence for left hand joints : 0 through 20
    # Sequence for right hand joints : 0 through 20
    


# Turn on pose mode and Auto IK (found in Pose Options in user interface)
# Set Auto-IK chain length to 1 (Shift-PageDn in user interface)

# ROOT BONES ==========================

# Find OpenPose root joint 0 position; OpXPos
# Find OpenPose root joint 0 position; OpYPos
# Store ScreenSpace root bone position; SsXPos
# Store ScreenSpace root bone position; SsYPos

# Change camera focal-length, height, orientation and location to user inputs

# Start LOOPS =====================================

# Frame Loop for number of video frames
    # Joint loop for number of joints
        # Read x and y data for joint(num) from OpenPose Json output file
        # For OpenPose JSON output format see: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/02_output.md
        # Reposition joint vertex
            # Calculate joint tip position in screen space
            
            # Move joint to new position

        # Read esc key
        # For debugging add one second delay
    # End joint loop
    # Increment progess bar 
    # Increment Blender frame
# End frame loop

# END LOOPS =====================================

# Save action

# Restores
    # Restore screen space mode; OrigSSMode
    # Restore screen space height; OrigSSHgt
    # Restore screen space width; OrigSSWid
    # Restore camera position, orientation and F-Stop properties if available
    # Restore character bones to rest position



# If moveable camera is desired then input start and end positions
