#Regan_Matt-CA01
#10/2017
#A program which takes user measurements and outputs calculations based on building a barge

bLength = float(input("What is the length of the barge (Metres): "))

bBreadth = float(input("What is the breadth of the barge (Metres): "))

bHeight = float(input("What is the height of the barge (Metres): "))

print ("===============================================================")

bArea = bLength * bBreadth

bSurfaceArea = (2 * bHeight) * (bLength + bBreadth) + (bArea)
bMass = bSurfaceArea * 1.06
bDraft = bMass/bArea


print ("The surface area of the barge is: ",round (bSurfaceArea,2),"m^2")

print ("---------------------------------------------------------------")

print ("The mass of the barge is: ",round(bMass,2),"kg")

print ("---------------------------------------------------------------")

print ("The resulting draft of the barge is: ",round(bDraft,2),"m")

input()

# L B H = Draft
# 1 2 3 = 10.6
# 2 3 4 = 8.13
# 12 18 6 = 2.83
