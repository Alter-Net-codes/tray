# imports
import os

# vars
Branches = []
Branch = 0
LastBranch = 0
ProjectName = 0
Icon = 0
LibNameLs = []
LibSrcLs = []
LibVerLs = []
LibName = 0
LastLib = 0
TimesLoopedBuildLibs = 0

# intro
print("please run this on a linux machine to build a poggit file.")

# get branches
while True:
  Branch = input("enter a branch to build from: ")
  Branches.append(Branch)
  LastBranch = input("is that the last branch? [yes/no]: ")
  if LastBranch == "yes":
    print("okay!")
    break
  else:
    print()

# get project name
ProjectName = input("enter the project name: ")

# get project icon
Icon = input("enter icon file name including file extension: ")

# get project libs
LibsTrue = input("are you intending to have libs? [yes/no]: ")
if LibsTrue == "yes":
    while True:
        LibName = input("enter a lib: ")
        LibSrc = input("enter the LibSrc: ")
        LibVer = input("enter the LibVer: ")
        LibNameLs.append(LibName)
        LibSrcLs.append(LibSrc)
        LibVerLs.append(LibVer)
        LastLib = input("is that the last lib? [yes/no]: ")
        if LastLib == "yes":
            print("okay!")
            break
        else:
            print()
else:
   print("okay!")

# Build the Poggit File
os.remove(".poggit.yml")
f = open(".poggit.yml", "x")
f = open(".poggit.yml", "a")
f.write("---")
# Build the branches section
f.write("branches:")
for branch in Branches:
    f.write(f"  - {branch}\n")
# Bulild the project name
f.write("projects:")
f.write(f"  {ProjectName}:")
# Build the project icons
f.write("    paths: ''")
f.write("    icon: {icon}")
# Build the libs
if LibsTrue == "yes":
    print(Libs)
    f.write("    libs:")
    for TimesLoopedBuildLibs in range(len(LibNameLs)):
        f.write(f"    - {LibNameLs[TimesLoopedBuildLibs]}")
        f.write(f"      - {LibSrcLs[TimesLoopedBuildLibs]}")
        f.write(f"      - {LibVerLs[TimesLoopedBuildLibs]}")
# end
print("done")
