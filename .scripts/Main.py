# vars
Branches = []
LastBranch = 0
ProjectName = 0
Icon = 0
Libs = []
LibName
LastLib = 0
TimesLoopedBuildLibs = 0

# intro
print("please run this on a linux machine to build a poggit file.")

# get branches
while True:
  Branch = input("enter a branch to build from: ")
  Branches.append(branch)
  LastBranch = input("is that the last branch? [yes/no]: ")
  if answer = "yes":
    print("okay!")
    break
  else:
    print()

# get project name
ProjectName = input("enter the project name: ")

# get project icon
Icon = input("enter icon file name including file extension: ")

# get project libs
while True
  LibName = input("enter a lib: ")
  LibSrc = input("enter the LibSrc: ")
  LibVer = input("enter the LibVer: ")
  Libs.append(LibName)
  Libs.append(LibSrc)
  Libs.append(LibVer)
  LastLib = input("is that the last lib? [yes/no]: ")
  if LastLib = "yes"
    print("okay!")
    break
  else:
    print()

# Build the Poggit File
f = open("poggit.yml", "x")
f = open("poggit.yml", "a")
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
f.write("    libs:")
for i in range(int(len(Libs))):
  f.write(f"    - {Libs[TimesLoopedBuildLibs]}\n")
  f.write(f"      - {Libs[TimesLoopedBuildLibs] + 1}\n")
  f.write(f"      - {Libs[TimesLoopedBuildLibs] + 2}\n")
  TimesLoopedBuildLibs += 3
# write the end
f.write("...")
