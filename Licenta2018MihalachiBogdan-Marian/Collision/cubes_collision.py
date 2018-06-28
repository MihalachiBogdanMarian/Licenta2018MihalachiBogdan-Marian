import math
import random

import maya.cmds as cmds

distanceSafeToJump = [4, 5]  # the distance from the target object so the horse can jump over it
maxHeightSafeToJumpOver = 2  # the maximum height over which the horse can jump
maxWidthSafeToJumpOver = 2  # the maximum length the horse can jump over
constraints = [distanceSafeToJump, maxHeightSafeToJumpOver, maxWidthSafeToJumpOver]


# returns the new coordinates of the point if the point has rotations applied to it around a center point
def rotatedPoint(rotations, point, center):
    rotatedPoint = point
    if rotations[0] != 0:
        rotatedPoint = [
            rotatedPoint[0],
            (rotatedPoint[1] - center[1]) * math.cos(math.pi * rotations[0] / 180) - (
                    rotatedPoint[2] - center[2]) * math.sin(
                math.pi * rotations[0] / 180) + center[1],
            (rotatedPoint[1] - center[1]) * math.sin(math.pi * rotations[0] / 180) + (
                    rotatedPoint[2] - center[2]) * math.cos(
                math.pi * rotations[0] / 180) + center[2]]
    if rotations[1] != 0:
        rotatedPoint = [
            (rotatedPoint[2] - center[2]) * math.sin(math.pi * rotations[1] / 180) + (rotatedPoint[
                                                                                          0] - center[0]) * math.cos(
                math.pi * rotations[1] / 180) + center[0],
            rotatedPoint[1],
            (rotatedPoint[2] - center[2]) * math.cos(math.pi * rotations[1] / 180) - (rotatedPoint[
                                                                                          0] - center[0]) * math.sin(
                math.pi * rotations[1] / 180) + center[2]]
    if rotations[2] != 0:
        rotatedPoint = [
            (rotatedPoint[0] - center[0]) * math.cos(math.pi * rotations[2] / 180) - (rotatedPoint[
                                                                                          1] - center[1]) * math.sin(
                math.pi * rotations[2] / 180) + center[0],
            (rotatedPoint[0] - center[0]) * math.sin(math.pi * rotations[2] / 180) + (rotatedPoint[
                                                                                          1] - center[1]) * math.cos(
                math.pi * rotations[2] / 180) + center[1],
            rotatedPoint[2]]
    for i in range(0, 3):
        if abs(rotatedPoint[i]) <= 10 ** (-10):
            rotatedPoint[i] = 0.0
    return rotatedPoint


# function which returns a vector containing the coordinates of the 8 points that form the rectangular box given as parameter
def corners(_object):
    corners = []
    cmds.select(_object)
    obj = cmds.ls(selection=True)[0]
    center = [cmds.getAttr(obj + ".translateX"), cmds.getAttr(obj + ".translateY"),
              cmds.getAttr(obj + ".translateZ")]
    rotations = [cmds.getAttr(obj + ".rotateX"), cmds.getAttr(obj + ".rotateY"),
                 cmds.getAttr(obj + ".rotateZ")]
    width = cmds.getAttr(obj + ".scaleX")
    height = cmds.getAttr(obj + ".scaleY")
    depth = cmds.getAttr(obj + ".scaleZ")

    rightTopFront = [center[0] + width / 2, center[1] + height / 2, center[2] + depth / 2]
    rightTopFront = rotatedPoint(rotations, rightTopFront, center)
    corners.append(rightTopFront)
    rightTopBack = [center[0] + width / 2, center[1] + height / 2, center[2] - depth / 2]
    rightTopBack = rotatedPoint(rotations, rightTopBack, center)
    corners.append(rightTopBack)
    rightDownBack = [center[0] + width / 2, center[1] - height / 2, center[2] - depth / 2]
    rightDownBack = rotatedPoint(rotations, rightDownBack, center)
    corners.append(rightDownBack)
    rightDownFront = [center[0] + width / 2, center[1] - height / 2, center[2] + depth / 2]
    rightDownFront = rotatedPoint(rotations, rightDownFront, center)
    corners.append(rightDownFront)

    leftTopFront = [center[0] - width / 2, center[1] + height / 2, center[2] + depth / 2]
    leftTopFront = rotatedPoint(rotations, leftTopFront, center)
    corners.append(leftTopFront)
    leftTopBack = [center[0] - width / 2, center[1] + height / 2, center[2] - depth / 2]
    leftTopBack = rotatedPoint(rotations, leftTopBack, center)
    corners.append(leftTopBack)
    leftDownBack = [center[0] - width / 2, center[1] - height / 2, center[2] - depth / 2]
    leftDownBack = rotatedPoint(rotations, leftDownBack, center)
    corners.append(leftDownBack)
    leftDownFront = [center[0] - width / 2, center[1] - height / 2, center[2] + depth / 2]
    leftDownFront = rotatedPoint(rotations, leftDownFront, center)
    corners.append(leftDownFront)

    return corners


# function which creates the walk animation
def objectWalk(_object, axis, minValue, maxValue, minFrame, maxFrame):
    cmds.select(_object)
    obj = cmds.ls(selection=True)[0]
    cmds.setKeyframe(obj + '.translate' + axis, value=minValue, time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj + '.translate' + axis, value=maxValue, time=maxFrame, inTangentType="linear",
                     outTangentType="linear")


# function which creates the jump animation
def objectJump(object1, object2, axis, constraints, direction, minFrame, maxFrame):
    cmds.select(object1)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX"), cmds.getAttr(obj1 + ".translateY"),
               cmds.getAttr(obj1 + ".translateZ")]
    width1 = cmds.getAttr(obj1 + ".scaleX")

    cmds.select(object2)
    obj2 = cmds.ls(selection=True)[0]
    height2 = cmds.getAttr(obj2 + ".scaleY")

    middleFrame = math.floor((maxFrame + minFrame) / 2)

    cmds.setKeyframe(obj1 + '.translate' + axis, value=(center1[0] if axis == 'X' else center1[2]), time=minFrame,
                     inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=center1[1], time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    if axis == "X":
        cmds.setKeyframe(obj1 + '.rotateZ', value=direction * 0, time=minFrame, inTangentType="linear",
                         outTangentType="linear")
    elif axis == "Z":
        cmds.setKeyframe(obj1 + '.rotateX', value=-direction * 90, time=minFrame, inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=minFrame,
                         inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=90, time=minFrame, inTangentType="linear",
                         outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=(center1[0] if axis == 'X' else center1[2]) + direction * (
            constraints[0][1] + width1 + maxWidthSafeToJumpOver) / 3,
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=(center1[1] + height2 + constraints[1] + 1) / 2,
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    if axis == "X":
        cmds.setKeyframe(obj1 + '.rotateZ', value=direction * 45, time=math.floor((middleFrame + minFrame) / 2),
                         inTangentType="linear", outTangentType="linear")
    elif axis == "Z":
        cmds.setKeyframe(obj1 + '.rotateX', value=-direction * 90, time=math.floor((middleFrame + minFrame) / 2),
                         inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") + direction * 45,
                         time=math.floor((middleFrame + minFrame) / 2), inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=90, time=math.floor((middleFrame + minFrame) / 2),
                         inTangentType="linear",
                         outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=(center1[0] if axis == 'X' else center1[2]) + direction * 2 * (
            constraints[0][1] + width1 + maxWidthSafeToJumpOver) / 3, time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=center1[1] + height2 + constraints[1] + 1,
                     time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    if axis == "X":
        cmds.setKeyframe(obj1 + '.rotateZ', value=direction * 0, time=middleFrame,
                         inTangentType="linear", outTangentType="linear")
    elif axis == "Z":
        cmds.setKeyframe(obj1 + '.rotateX', value=-direction * 90, time=middleFrame, inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=middleFrame,
                         inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=90, time=middleFrame, inTangentType="linear",
                         outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=(center1[0] if axis == 'X' else center1[2]) + direction * (
            constraints[0][1] + width1 + maxWidthSafeToJumpOver),
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=(center1[1] + height2 + constraints[1] + 1) / 2,
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    if axis == "X":
        cmds.setKeyframe(obj1 + '.rotateZ', value=-45 * direction, time=math.floor((maxFrame + middleFrame) / 2),
                         inTangentType="linear", outTangentType="linear")
    elif axis == "Z":
        cmds.setKeyframe(obj1 + '.rotateX', value=-direction * 90, time=math.floor((maxFrame + middleFrame) / 2),
                         inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") - direction * 45,
                         time=math.floor((maxFrame + middleFrame) / 2), inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=90, time=math.floor((maxFrame + middleFrame) / 2),
                         inTangentType="linear",
                         outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=(center1[0] if axis == 'X' else center1[2]) + direction * 4 * (
            constraints[0][1] + width1 + maxWidthSafeToJumpOver) / 3,
                     time=maxFrame,
                     inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=center1[1], time=maxFrame, inTangentType="linear",
                     outTangentType="linear")
    if axis == "X":
        cmds.setKeyframe(obj1 + '.rotateZ', value=direction * 0, time=maxFrame, inTangentType="linear",
                         outTangentType="linear")
    elif axis == "Z":
        cmds.setKeyframe(obj1 + '.rotateX', value=-direction * 90, time=maxFrame, inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=maxFrame,
                         inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=90, time=maxFrame, inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateX', value=0, time=maxFrame + 1, inTangentType="linear",
                         outTangentType="linear")
        cmds.setKeyframe(obj1 + '.rotateZ', value=0, time=maxFrame + 1, inTangentType="linear",
                         outTangentType="linear")


# function which creates the dodge animation
def objectDodge(object1, object2, axis, direction, minFrame, maxFrame):
    cmds.select(object1)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX"), cmds.getAttr(obj1 + ".translateY"),
               cmds.getAttr(obj1 + ".translateZ")]

    cmds.select(object2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]
    width2 = cmds.getAttr(obj2 + ".scaleX")

    middleFrame = math.floor((maxFrame + minFrame) / 2)

    upDown = random.randint(0, 1)
    upDownPointXZ = startPointXZ = endPointXZ = firstChangePointXZ = secondChangePointXZ = []
    if axis == "X":
        if upDown == 0:  # up, Z negative
            upDownPointXZ = [(corners(obj2)[1][0] + corners(obj2)[5][0]) / 2,
                             corners(obj2)[1][2] - direction * (1 + width2)]
        else:  # down, Z positive  
            upDownPointXZ = [(corners(obj2)[0][0] + corners(obj2)[4][0]) / 2,
                             corners(obj2)[0][2] + direction * (1 + width2)]
        startPointXZ = [center1[0], center1[2]]
        endPointXZ = [upDownPointXZ[0] + (upDownPointXZ[0] - startPointXZ[0]), center1[2]]
        if upDown == 0:
            firstChangePointXZ = [(center2[0] - startPointXZ[0]) * math.cos(math.pi * 135 / 180) + center2[0],
                                  (upDownPointXZ[1] - center2[2]) * math.sin(math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [upDownPointXZ[0] + (upDownPointXZ[0] - firstChangePointXZ[0]), firstChangePointXZ[1]]
        else:
            firstChangePointXZ = [(center2[0] - startPointXZ[0]) * math.cos(-math.pi * 135 / 180) + center2[0],
                                  (center2[2] - upDownPointXZ[1]) * math.sin(-math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [upDownPointXZ[0] + (upDownPointXZ[0] - firstChangePointXZ[0]), firstChangePointXZ[1]]
    elif axis == "Z":
        if upDown == 0:  # up, X positive
            upDownPointXZ = [corners(obj2)[1][0] + direction * 2, center2[2]]
        else:  # down, X negative 
            upDownPointXZ = [corners(obj2)[0][0] - direction * 2, center2[2]]
        startPointXZ = [center1[0], center1[2]]
        endPointXZ = [center1[0], upDownPointXZ[1] + (upDownPointXZ[1] - startPointXZ[1])]
        if upDown == 0:
            firstChangePointXZ = [(upDownPointXZ[0] - center2[0]) * math.sin(math.pi * 135 / 180) + center2[0],
                                  (center2[2] - startPointXZ[1]) * math.cos(math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [firstChangePointXZ[0], upDownPointXZ[1] + (upDownPointXZ[1] - firstChangePointXZ[1])]
        else:
            firstChangePointXZ = [(center2[0] - upDownPointXZ[0]) * math.sin(-math.pi * 135 / 180) + center2[0],
                                  (center2[2] - startPointXZ[1]) * math.cos(-math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [firstChangePointXZ[0], upDownPointXZ[1] + (upDownPointXZ[1] - firstChangePointXZ[1])]

    cmds.setKeyframe(obj1 + '.translateX', value=startPointXZ[0], time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=startPointXZ[1], time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=minFrame,
                     inTangentType="linear",
                     outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=firstChangePointXZ[0],
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=firstChangePointXZ[1],
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") + 45 if upDown == 0 else
    cmds.getAttr(obj1 + ".rotateY") - 45, time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=upDownPointXZ[0], time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=upDownPointXZ[1], time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=middleFrame,
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=secondChangePointXZ[0],
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=secondChangePointXZ[1],
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") - 45 if upDown == 0 else
    cmds.getAttr(obj1 + ".rotateY") + 45, time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=endPointXZ[0], time=maxFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=endPointXZ[1], time=maxFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=maxFrame,
                     inTangentType="linear",
                     outTangentType="linear")


# verifies if a value is between two given limits
def inRange(value, minValue, maxValue):
    return value >= min(minValue, maxValue) and value <= max(minValue, maxValue)


# verifies if two intervals are overlapping or not
def rangeIntersect(min1, max1, min2, max2):
    return max(min1, max1) >= min(min2, max2) and min(min1, max1) <= max(min2, max2)


# verifies the collision point-rectangular box if the box isn't rotated
def pointBoxCollision(x, y, z, box):
    cmds.select(box)
    obj = cmds.ls(selection=True)[0]
    rightTopFront = corners(obj)[0]
    rightTopBack = corners(obj)[1]
    leftTopFront = corners(obj)[4]
    rightDownFront = corners(obj)[3]

    return inRange(x, rightTopFront[0], leftTopFront[0]) and \
           inRange(y, rightTopFront[1], rightDownFront[1]) and \
           inRange(z, rightTopFront[2], rightTopBack[2])


# cmds.select("pPlane1")
# planeObj = cmds.ls(selection=True)[0]


# print(pointBoxCollision(cmds.getAttr(planeObj + ".translateX"), cmds.getAttr(planeObj + ".translateY"),
#                        cmds.getAttr(planeObj + ".translateZ"), "pCube2"))

# verifies the collision box-box without them having rotations applied
def boxesCollisionNoRotations(box1, box2, xDistance, zDistance, direction):
    cmds.select(box1)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX"), cmds.getAttr(obj1 + ".translateY"),
               cmds.getAttr(obj1 + ".translateZ")]
    rotations1 = [cmds.getAttr(obj1 + ".rotateX"), cmds.getAttr(obj1 + ".rotateY"),
                  cmds.getAttr(obj1 + ".rotateZ")]
    width1 = cmds.getAttr(obj1 + ".scaleX")
    height1 = cmds.getAttr(obj1 + ".scaleY")
    depth1 = cmds.getAttr(obj1 + ".scaleZ")
    rightTopFront1 = [center1[0] + width1 / 2, center1[1] + height1 / 2, center1[2] + depth1 / 2]
    rightTopFront1 = rotatedPoint(rotations1, rightTopFront1, center1)

    cmds.select(box2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]
    rotations2 = [cmds.getAttr(obj2 + ".rotateX"), cmds.getAttr(obj2 + ".rotateY"),
                  cmds.getAttr(obj2 + ".rotateZ")]
    width2 = cmds.getAttr(obj2 + ".scaleX")
    height2 = cmds.getAttr(obj2 + ".scaleY")
    depth2 = cmds.getAttr(obj2 + ".scaleZ")
    rightTopFront2 = [center2[0] + width2 / 2, center2[1] + height2 / 2, center2[2] + depth2 / 2]
    rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)

    if xDistance != 0:
        return rangeIntersect(rightTopFront1[0] + direction * xDistance,
                              rightTopFront1[0] + direction * xDistance - direction * width1, rightTopFront2[0],
                              rightTopFront2[0] - direction * width2) and \
               rangeIntersect(rightTopFront1[1], rightTopFront1[1] - height1, rightTopFront2[1],
                              rightTopFront2[1] - height2) and \
               rangeIntersect(rightTopFront1[2] + direction * zDistance,
                              rightTopFront1[2] + direction * zDistance - direction * depth1, rightTopFront2[2],
                              rightTopFront2[2] - direction * depth2)
    elif zDistance != 0:
        return rangeIntersect(rightTopFront1[0] + direction * xDistance,
                              rightTopFront1[0] + direction * xDistance + direction * depth1, rightTopFront2[0],
                              rightTopFront2[0] + direction * depth2) and \
               rangeIntersect(rightTopFront1[1], rightTopFront1[1] - height1, rightTopFront2[1],
                              rightTopFront2[1] - height2) and \
               rangeIntersect(rightTopFront1[2] + direction * zDistance,
                              rightTopFront1[2] + direction * zDistance - direction * width1, rightTopFront2[2],
                              rightTopFront2[2] - direction * width2)


# print(boxesCollisionNoRotations("pCube1", "pCube2", 3, 0, 0))

# verifies if the first box satisfies the conditions which allow it to jump over the second box
# if not, it will verify if the box can pass by the object
def checkIfCanJump(box1, box2, constraints, axis, direction):
    cmds.select(box1)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX"), cmds.getAttr(obj1 + ".translateY"),
               cmds.getAttr(obj1 + ".translateZ")]
    width1 = cmds.getAttr(obj1 + ".scaleX")
    height1 = cmds.getAttr(obj1 + ".scaleY")
    depth1 = cmds.getAttr(obj1 + ".scaleZ")
    rightTopFront1 = [center1[0] + width1 / 2, center1[1] + height1 / 2, center1[2] + depth1 / 2]

    cmds.select(box2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]
    width2 = cmds.getAttr(obj2 + ".scaleX")
    height2 = cmds.getAttr(obj2 + ".scaleY")
    depth2 = cmds.getAttr(obj2 + ".scaleZ")
    rightTopFront2 = [center2[0] + width2 / 2, center2[1] + height2 / 2, center2[2] + depth2 / 2]

    return boxesCollisionNoRotations(box1, box2, constraints[0][1] if axis == "X" else 0,
                                     constraints[0][1] if axis == "Z" else 0, direction) and \
           not boxesCollisionNoRotations(box1, box2, constraints[0][0] if axis == "X" else 0,
                                         constraints[0][0] if axis == "Z" else 0, direction) and \
           width2 <= constraints[2] and \
           rightTopFront1[1] - rightTopFront2[1] >= constraints[1]


print(checkIfCanJump("pCube1", "pCube2", constraints, "Z", -1))
# objectJump("pCube1", "pCube2", "Z", constraints, -1, 15, 36)
objectDodge("pCube1", "pCube2", "Z", -1, 15, 36)
objectWalk("pCube1", "Z", 20, -20, 1, 50)
