import math
import random

import maya.cmds as cmds

distanceSafeToJump = [5, 9]  # the distance from the target object so the horse can jump over it
maxHeightSafeToJumpOver = 3  # the maximum height over which the horse can jump
maxWidthSafeToJumpOver = 5  # the maximum length the horse can jump over
constraints = [distanceSafeToJump, maxHeightSafeToJumpOver, maxWidthSafeToJumpOver]

# values to be subtracted or added to the horse translation attributes
# because the horse was realized a little moved from the center of the grid
horseYDisplacement = 5.514
horseControlXDisplacement = 1.518
horseControlZDisplacement = -4.886
displacements = [horseControlXDisplacement, horseYDisplacement, horseControlZDisplacement]


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
def corners(_object, axis, direction):
    corners = []
    cmds.select(_object)
    obj = cmds.ls(selection=True)[0]
    center = [cmds.getAttr(obj + ".translateX"), cmds.getAttr(obj + ".translateY"),
              cmds.getAttr(obj + ".translateZ")]
    rotations = [cmds.getAttr(obj + ".rotateX"), cmds.getAttr(obj + ".rotateY"),
                 cmds.getAttr(obj + ".rotateZ")]

    objectBoundingBox = cmds.xform(_object, q=True, bb=True)
    width = abs(objectBoundingBox[3] - objectBoundingBox[0])
    height = abs(objectBoundingBox[4] - objectBoundingBox[1])
    depth = abs(objectBoundingBox[5] - objectBoundingBox[2])

    if axis == "X" and direction == 1 and (179 <= rotations[1] <= 181 or -181 <= rotations[1] <= -179):
        rotations[1] = 0
    elif axis == "X" and direction == -1 and -1 <= rotations[1] <= 1:
        rotations[1] = 180
    elif axis == "Z" and direction == 1 and 89 <= rotations[1] <= 91:
        rotations[1] = -90
    elif axis == "Z" and direction == -1 and -91 <= rotations[1] <= -89:
        rotations[1] = 90

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
def objectJump(object1, object1Control, object2, axis, direction, minFrame, maxFrame):
    cmds.select(object1Control)
    obj1 = cmds.ls(selection=True)[0]

    object1BoundingBox = cmds.xform(object1, q=True, bb=True)
    width1 = abs(object1BoundingBox[3] - object1BoundingBox[0])
    # height1 = abs(object1BoundingBox[4] - object1BoundingBox[1])
    depth1 = abs(object1BoundingBox[5] - object1BoundingBox[2])

    center1 = [cmds.getAttr(obj1 + ".translateX") - displacements[0],
               cmds.getAttr(obj1 + ".translateY") + displacements[1],
               cmds.getAttr(obj1 + ".translateZ") - displacements[2]]

    cmds.select(object2)
    # obj2 = cmds.ls(selection=True)[0]

    object2BoundingBox = cmds.xform(object2, q=True, bb=True)
    # width2 = abs(object2BoundingBox[3] - object2BoundingBox[0])
    height2 = abs(object2BoundingBox[4] - object2BoundingBox[1])
    # depth2 = abs(object2BoundingBox[5] - object2BoundingBox[2])

    middleFrame = math.floor((maxFrame + minFrame) / 2)

    cmds.setKeyframe(obj1 + '.translate' + axis,
                     value=((center1[0] + displacements[0]) if axis == 'X' else (center1[2] + displacements[2])),
                     time=minFrame,
                     inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=(center1[1] - displacements[1]), time=minFrame, inTangentType="linear",
                     outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=((center1[0] + displacements[0]) if axis == 'X' else (
            center1[2] + displacements[2])) + direction * (
                                                               constraints[0][1] + (
                                                           width1 if axis == "X" else depth1) + maxWidthSafeToJumpOver) / 3,
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=((center1[1] - displacements[1]) + height2 + constraints[1] + 1) / 2,
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=((center1[0] + displacements[0]) if axis == 'X' else (
            center1[2] + displacements[2])) + direction * 2 * (
                                                               constraints[0][1] + (
                                                           width1 if axis == "X" else depth1) + maxWidthSafeToJumpOver) / 3,
                     time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=(center1[1] - displacements[1]) + height2 + constraints[1] + 1,
                     time=middleFrame,
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=((center1[0] + displacements[0]) if axis == 'X' else (
            center1[2] + displacements[2])) + direction * (
                                                               constraints[0][1] + (
                                                           width1 if axis == "X" else depth1) + maxWidthSafeToJumpOver),
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=((center1[1] - displacements[1]) + height2 + constraints[1] + 1) / 2,
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translate' + axis, value=((center1[0] + displacements[0]) if axis == 'X' else (
            center1[2] + displacements[2])) + direction * 4 * (
                                                               constraints[0][1] + (
                                                           width1 if axis == "X" else depth1) + maxWidthSafeToJumpOver) / 3,
                     time=maxFrame,
                     inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateY', value=(center1[1] - displacements[1]), time=maxFrame, inTangentType="linear",
                     outTangentType="linear")


# function which creates the dodge animation
def objectDodge(object1, object1Control, object2, axis, direction, minFrame, maxFrame):
    cmds.select(object1Control)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX") - displacements[0],
               cmds.getAttr(obj1 + ".translateY") + displacements[1],
               cmds.getAttr(obj1 + ".translateZ") - displacements[2]]

    cmds.select(object2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]

    object2BoundingBox = cmds.xform(object2, q=True, bb=True)
    width2 = abs(object2BoundingBox[3] - object2BoundingBox[0])

    middleFrame = math.floor((maxFrame + minFrame) / 2)

    upDown = random.randint(0, 1)
    upDownPointXZ = startPointXZ = endPointXZ = firstChangePointXZ = secondChangePointXZ = []
    if axis == "X":
        if upDown == 0:  # up, Z negative
            upDownPointXZ = [(corners(obj2, axis, direction)[1][0] + corners(obj2, axis, direction)[5][0]) / 2,
                             corners(obj2, axis, direction)[1][2] - direction * (1 + width2 / 2)]
        else:  # down, Z positive  
            upDownPointXZ = [(corners(obj2, axis, direction)[0][0] + corners(obj2, axis, direction)[4][0]) / 2,
                             corners(obj2, axis, direction)[0][2] + direction * (1 + width2 / 2)]
        startPointXZ = [(center1[0]), (center1[2])]
        endPointXZ = [upDownPointXZ[0] + (upDownPointXZ[0] - startPointXZ[0]), (center1[2])]
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
            upDownPointXZ = [corners(obj2, axis, direction)[1][0] + direction * (1 + width2 / 2), center2[2]]
            print(upDownPointXZ)
        else:  # down, X negative 
            upDownPointXZ = [corners(obj2, axis, direction)[0][0] - direction * (1 + width2 / 2), center2[2]]
        startPointXZ = [(center1[0]), (center1[2])]
        endPointXZ = [(center1[0]), upDownPointXZ[1] + (upDownPointXZ[1] - startPointXZ[1])]
        if upDown == 0:
            firstChangePointXZ = [(upDownPointXZ[0] - center2[0]) * math.sin(math.pi * 135 / 180) + center2[0],
                                  (center2[2] - startPointXZ[1]) * math.cos(math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [firstChangePointXZ[0], upDownPointXZ[1] + (upDownPointXZ[1] - firstChangePointXZ[1])]
        else:
            firstChangePointXZ = [(center2[0] - upDownPointXZ[0]) * math.sin(-math.pi * 135 / 180) + center2[0],
                                  (center2[2] - startPointXZ[1]) * math.cos(-math.pi * 135 / 180) + center2[2]]
            secondChangePointXZ = [firstChangePointXZ[0], upDownPointXZ[1] + (upDownPointXZ[1] - firstChangePointXZ[1])]

    cmds.setKeyframe(obj1 + '.translateX', value=startPointXZ[0] - displacements[0], time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=startPointXZ[1] - displacements[1], time=minFrame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=minFrame,
                     inTangentType="linear",
                     outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=firstChangePointXZ[0] - displacements[0],
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=firstChangePointXZ[1] - displacements[1],
                     time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") + 45 if upDown == 0 else
    cmds.getAttr(obj1 + ".rotateY") - 45, time=math.floor((middleFrame + minFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=upDownPointXZ[0] - displacements[0], time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=upDownPointXZ[1] - displacements[1], time=middleFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY"), time=middleFrame,
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=secondChangePointXZ[0] - displacements[0],
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=secondChangePointXZ[1] - displacements[1],
                     time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.rotateY', value=cmds.getAttr(obj1 + ".rotateY") - 45 if upDown == 0 else
    cmds.getAttr(obj1 + ".rotateY") + 45, time=math.floor((maxFrame + middleFrame) / 2),
                     inTangentType="linear", outTangentType="linear")

    cmds.setKeyframe(obj1 + '.translateX', value=endPointXZ[0] - displacements[0], time=maxFrame,
                     inTangentType="linear", outTangentType="linear")
    cmds.setKeyframe(obj1 + '.translateZ', value=endPointXZ[1] - displacements[1], time=maxFrame, inTangentType="linear",
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


# verifies the collision box-box without them having rotations applied
def boxesCollisionNoRotations(box1, box1Control, box2, xDistance, zDistance, direction):
    cmds.select(box1Control)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX") - displacements[0],
               cmds.getAttr(obj1 + ".translateY") + displacements[1],
               cmds.getAttr(obj1 + ".translateZ") - displacements[2]]
    rotations1 = [cmds.getAttr(obj1 + ".rotateX"), cmds.getAttr(obj1 + ".rotateY"),
                  cmds.getAttr(obj1 + ".rotateZ")]

    object1BoundingBox = cmds.xform(box1, q=True, bb=True)
    width1 = abs(object1BoundingBox[3] - object1BoundingBox[0])
    height1 = abs(object1BoundingBox[4] - object1BoundingBox[1])
    depth1 = abs(object1BoundingBox[5] - object1BoundingBox[2])

    rightTopFront1 = [center1[0] + width1 / 2, center1[1] + height1 / 2,
                      center1[2] + depth1 / 2] if xDistance != 0 else [center1[0] + depth1 / 2,
                                                                       center1[1] + height1 / 2,
                                                                       center1[2] + width1 / 2]
    rightTopFront1 = rotatedPoint(rotations1, rightTopFront1, center1)

    cmds.select(box2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]
    rotations2 = [cmds.getAttr(obj2 + ".rotateX"), cmds.getAttr(obj2 + ".rotateY"),
                  cmds.getAttr(obj2 + ".rotateZ")]

    object2BoundingBox = cmds.xform(box2, q=True, bb=True)
    width2 = abs(object2BoundingBox[3] - object2BoundingBox[0])
    height2 = abs(object2BoundingBox[4] - object2BoundingBox[1])
    depth2 = abs(object2BoundingBox[5] - object2BoundingBox[2])

    rightTopFront2 = [center2[0] + width2 / 2, center2[1] + height2 / 2,
                      center2[2] + depth2 / 2] if xDistance != 0 else [center2[0] + depth2 / 2,
                                                                       center2[1] + height2 / 2,
                                                                       center2[2] + width2 / 2]

    if xDistance != 0 and direction == 1 and (rotations2[1] == 180 or rotations2[1] == -180):
        rotations2[1] = 0
        rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)
    elif xDistance != 0 and direction == -1 and rotations2[1] == 0:
        rotations2[1] = 180
        rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)
    elif zDistance != 0 and direction == 1 and rotations2[1] == 90:
        rotations2[1] = -90
        rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)
    elif zDistance != 0 and direction == -1 and rotations2[1] == -90:
        rotations2[1] = 90
        rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)
    else:
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
                              rightTopFront1[0] + direction * xDistance + direction * width1, rightTopFront2[0],
                              rightTopFront2[0] + direction * width2) and \
               rangeIntersect(rightTopFront1[1], rightTopFront1[1] - height1, rightTopFront2[1],
                              rightTopFront2[1] - height2) and \
               rangeIntersect(rightTopFront1[2] + direction * zDistance,
                              rightTopFront1[2] + direction * zDistance - direction * depth1, rightTopFront2[2],
                              rightTopFront2[2] - direction * depth2)


# verifies if the first box satisfies the conditions which allow it to jump over the second box
# if not, it will verify if the box can pass by the object
def checkIfCanJump(box1, box1Control, box2, axis, direction):
    cmds.select(box1Control)
    obj1 = cmds.ls(selection=True)[0]
    center1 = [cmds.getAttr(obj1 + ".translateX") - displacements[0],
               cmds.getAttr(obj1 + ".translateY") + displacements[1],
               cmds.getAttr(obj1 + ".translateZ") - displacements[2]]
    rotations1 = [cmds.getAttr(obj1 + ".rotateX"), cmds.getAttr(obj1 + ".rotateY"),
                  cmds.getAttr(obj1 + ".rotateZ")]

    object1BoundingBox = cmds.xform(box1, q=True, bb=True)
    width1 = abs(object1BoundingBox[3] - object1BoundingBox[0])
    height1 = abs(object1BoundingBox[4] - object1BoundingBox[1])
    depth1 = abs(object1BoundingBox[5] - object1BoundingBox[2])

    rightTopFront1 = [center1[0] + width1 / 2, center1[1] + height1 / 2, center1[2] + depth1 / 2] if axis == "X" else [
        center1[0] + depth1 / 2, center1[1] + height1 / 2, center1[2] + width1 / 2]
    rightTopFront1 = rotatedPoint(rotations1, rightTopFront1, center1)

    cmds.select(box2)
    obj2 = cmds.ls(selection=True)[0]
    center2 = [cmds.getAttr(obj2 + ".translateX"), cmds.getAttr(obj2 + ".translateY"),
               cmds.getAttr(obj2 + ".translateZ")]
    rotations2 = [cmds.getAttr(obj2 + ".rotateX"), cmds.getAttr(obj2 + ".rotateY"),
                  cmds.getAttr(obj2 + ".rotateZ")]

    object2BoundingBox = cmds.xform(box2, q=True, bb=True)
    width2 = abs(object2BoundingBox[3] - object2BoundingBox[0])
    height2 = abs(object2BoundingBox[4] - object2BoundingBox[1])
    depth2 = abs(object2BoundingBox[5] - object2BoundingBox[2])

    rightTopFront2 = [center2[0] + width2 / 2, center2[1] + height2 / 2, center2[2] + depth2 / 2] if axis == "X" else [
        center2[0] + depth2 / 2, center2[1] + height2 / 2, center2[2] + width2 / 2]
    rightTopFront2 = rotatedPoint(rotations2, rightTopFront2, center2)

    return boxesCollisionNoRotations(box1, box1Control, box2, constraints[0][1] if axis == "X" else 0,
                                     constraints[0][1] if axis == "Z" else 0, direction) and \
           not boxesCollisionNoRotations(box1, box1Control, box2, constraints[0][0] if axis == "X" else 0,
                                         constraints[0][0] if axis == "Z" else 0, direction) and \
           (width2 if axis == "X" else depth2) <= constraints[2] and \
           rightTopFront1[1] - rightTopFront2[1] >= constraints[1]

# print(checkIfCanJump("horse_walk:horse", "horse_walk:nurbsCircle5", "pillar1:pillar", "X", 1))
# objectJump("horse_walk:horse", "horse_walk:nurbsCircle5", "pillar1:pillar", "X", 1, 15, 36)
# objectDodge("horse_walk:horse", "horse_walk:nurbsCircle5", "pillar1:pillar", "X", 1, 15, 36)
# objectWalk("horse_walk:nurbsCircle5", "X", -50, 50, 1, 50)
