# Blender-plugin-for-OpenPose-import

Various programs exist to import mocap into Blender 3D, but each has its limitations.  The purpose of this plugin is to allow Blender users to input mocap data they can create in the form of .json files from OpenPose. The computational power of Blender's IK engine will sequentially place the bone ends from root to fingertips and feet using x and y positions from OpenPose for each frame.

The plugin asks the user for camera data to loosely match the camera used to create the video input for generating an openpose output file.  It then proceeds to move each bone end into position using a window the plugin sets up to mimic the input window size specified in the OpenPose calculation.

This approach to convert any character movement video into an armature action should make a great popular Blender plugin.  Code contributions are welcome.
