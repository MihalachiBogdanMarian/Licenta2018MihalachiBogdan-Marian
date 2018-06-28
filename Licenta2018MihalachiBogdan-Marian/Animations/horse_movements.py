import maya.cmds as cmds


def horseWalk(nrOfAnimationRepetitions, startFrame):
    print("Walk")
    # RIGHT FRONT LEG AND KNEE
    cmds.select("nurbsCircle2")
    rightFrontFootControl = cmds.ls(selection=True)[0]
    print(cmds.objectType(rightFrontFootControl))

    startTime = cmds.playbackOptions(query=True, minTime=True)
    endTime = cmds.playbackOptions(query=True, maxTime=True)
    print(startTime - endTime)

    frame = startFrame
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=0, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.translateY', value=0, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.rotateZ', value=0, time=frame, inTangentType="linear",
                     outTangentType="linear")

    frame += 1
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=0.72, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.translateY', value=0.47, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.rotateZ', value=-51.16, time=frame, inTangentType="linear",
                     outTangentType="linear")

    frame += 1
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=1.81, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.translateY', value=-1.6, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.rotateZ', value=-51.16, time=frame, inTangentType="linear",
                     outTangentType="linear")

    frame += 1
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=0.7, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.translateY', value=-1.6, time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightFrontFootControl + '.rotateZ', value=0, time=frame, inTangentType="linear",
                     outTangentType="linear")

    translateXs = [0, -1.1, -1.89, -1.89, -1.05, 0.72, 1.81, 0.70]
    translateYs = [0, 0, 0, 0, 0.34, 0.47, -1.6, -1.6]
    rotateXs = [0, 0, 0, 0.57, 0.95, 0, 0, 0]
    rotateYs = [0, 0, 0, -1.02, -0.67, 0, 0, 0]
    rotateZs = [0, 0, 0, -58.36, -83.95, -51.16, -51.16, 0]
    for i in range(0, nrOfAnimationRepetitions):
        for j in range(0, 8):
            frame += 1
            cmds.setKeyframe(rightFrontFootControl + '.translateX', value=translateXs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(rightFrontFootControl + '.translateY', value=translateYs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(rightFrontFootControl + '.rotateX', value=rotateXs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(rightFrontFootControl + '.rotateY', value=rotateYs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(rightFrontFootControl + '.rotateZ', value=rotateZs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")

    cmds.select("nurbsCircle23")
    rightFrontKneeControl = cmds.ls(selection=True)[0]
    for i in range(0, nrOfAnimationRepetitions * 2):
        for j in range(0, 2):
            if j == 0:
                val = 0 if i % 2 == 1 else 2.80
                cmds.setKeyframe(rightFrontKneeControl + '.translateX', value=val, time=4 * i, inTangentType="linear",
                                 outTangentType="linear")
            else:
                val = 2.80 if i % 2 == 1 else 0
                cmds.setKeyframe(rightFrontKneeControl + '.translateX', value=val, time=4 * i + 1,
                                 inTangentType="linear", outTangentType="linear")

    # LEFT FRONT LEG AND KNEE 
    cmds.select("nurbsCircle6")
    leftFrontFootControl = cmds.ls(selection=True)[0]
    frame = startFrame - 1
    for i in range(0, nrOfAnimationRepetitions):
        for j in range(0, 8):
            frame += 1
            cmds.setKeyframe(leftFrontFootControl + '.translateX', value=translateXs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftFrontFootControl + '.translateY', value=translateYs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftFrontFootControl + '.rotateX', value=rotateXs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftFrontFootControl + '.rotateY', value=rotateYs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftFrontFootControl + '.rotateZ', value=rotateZs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")

    cmds.select("nurbsCircle24")
    leftFrontKneeControl = cmds.ls(selection=True)[0]
    for i in range(0, nrOfAnimationRepetitions * 2):
        for j in range(0, 2):
            if j == 0:
                val = 0 if i % 2 == 0 else 2.80
                cmds.setKeyframe(leftFrontKneeControl + '.translateX', value=val, time=4 * i, inTangentType="linear",
                                 outTangentType="linear")
            else:
                val = 2.80 if i % 2 == 0 else 0
                cmds.setKeyframe(leftFrontKneeControl + '.translateX', value=val, time=4 * i + 1,
                                 inTangentType="linear", outTangentType="linear")

    # RIGHT BACK LEG AND KNEE
    cmds.select("nurbsCircle1")
    rightBackFootControl = cmds.ls(selection=True)[0]
    # print(cmds.objectType(rightBackFootControl))

    frame = startFrame
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=0, time=frame, inTangentType="linear",
                     outTangentType="linear")

    frame += 1
    cmds.setKeyframe(rightFrontFootControl + '.translateX', value=1.26, time=frame, inTangentType="linear",
                     outTangentType="linear")

    translateXs = [0, -0.45, -0.98, -1.59, -0.52, 0.90, 3.51, 1.26]
    translateYs = [0, 0, 0, 0, 0.60, 0.60, 0.08, 0]
    rotateXs = [0, 0, 0, 0, 0, -1.95, -1.95, 0]
    rotateYs = [0, 0, 0, 0, 0, 1.23, 1.23, 0]
    rotateZs = [0, 0, 0, 0, -47.22, -28.41, -28.41, 0]
    for i in range(0, nrOfAnimationRepetitions):
        for j in range(0, 8):
            frame += 1
            cmds.setKeyframe(rightBackFootControl + '.translateX', value=translateXs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(rightBackFootControl + '.translateY', value=translateYs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(rightBackFootControl + '.rotateX', value=rotateXs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(rightBackFootControl + '.rotateY', value=rotateYs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(rightBackFootControl + '.rotateZ', value=rotateZs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")

    cmds.select("nurbsCircle25")
    rightBackKneeControl = cmds.ls(selection=True)[0]
    cmds.setKeyframe(rightBackKneeControl + '.translateZ', value=0, time=0, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightBackKneeControl + '.translateZ', value=-0.11, time=1, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(rightBackFootControl + '.translateZ', value=0, time=2, inTangentType="linear",
                     outTangentType="linear")
    for i in range(0, nrOfAnimationRepetitions * 2):
        for j in range(0, 2):
            if j == 0:
                cmds.setKeyframe(rightBackKneeControl + '.translateX', value=0, time=5 + 8 * i, inTangentType="linear",
                                 outTangentType="linear")
                cmds.setKeyframe(rightBackKneeControl + '.translateY', value=0, time=5 + 8 * i, inTangentType="linear",
                                 outTangentType="linear")
            else:
                cmds.setKeyframe(rightBackKneeControl + '.translateX', value=-3.32, time=5 + 8 * i + 1,
                                 inTangentType="linear", outTangentType="linear")
                cmds.setKeyframe(rightBackKneeControl + '.translateY', value=-3.59, time=5 + 8 * i + 1,
                                 inTangentType="linear", outTangentType="linear")

    # LEFT BACK LEG AND KNEE
    cmds.select("nurbsCircle7")
    leftBackFootControl = cmds.ls(selection=True)[0]
    # print(cmds.objectType(leftBackFootControl))

    frame = startFrame - 1
    for i in range(0, 6):
        frame += 1
        if i == 0:
            cmds.setKeyframe(leftBackFootControl + '.translateX', value=0, time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.translateY', value=0, time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateX', value=0, time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateY', value=0, time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateZ', value=0, time=frame, inTangentType="linear",
                             outTangentType="linear")
        else:
            cmds.setKeyframe(leftBackFootControl + '.translateX', value=translateXs[i + 2], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.translateY', value=translateYs[i + 2], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateX', value=rotateXs[i + 2], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateY', value=rotateYs[i + 2], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateZ', value=rotateZs[i + 2], time=frame,
                             inTangentType="linear", outTangentType="linear")

    for i in range(0, nrOfAnimationRepetitions):
        for j in range(0, 8):
            frame += 1
            cmds.setKeyframe(leftBackFootControl + '.translateX', value=translateXs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.translateY', value=translateYs[j], time=frame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateX', value=rotateXs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateY', value=rotateYs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")
            cmds.setKeyframe(leftBackFootControl + '.rotateZ', value=rotateZs[j], time=frame, inTangentType="linear",
                             outTangentType="linear")

    cmds.select("nurbsCircle26")
    leftBackKneeControl = cmds.ls(selection=True)[0]
    for i in range(0, nrOfAnimationRepetitions * 2):
        for j in range(0, 2):
            if j == 0:
                cmds.setKeyframe(leftBackKneeControl + '.translateX', value=0, time=1 + 8 * i, inTangentType="linear",
                                 outTangentType="linear")
                cmds.setKeyframe(leftBackKneeControl + '.translateY', value=0, time=1 + 8 * i, inTangentType="linear",
                                 outTangentType="linear")
            else:
                cmds.setKeyframe(leftBackKneeControl + '.translateX', value=-3.32, time=1 + 8 * i + 1,
                                 inTangentType="linear", outTangentType="linear")
                cmds.setKeyframe(leftBackKneeControl + '.translateY', value=-3.59, time=1 + 8 * i + 1,
                                 inTangentType="linear", outTangentType="linear")


def horseActionKeySetForBodySegment(translationsRotations, control, frame):
    cmds.setKeyframe(control + '.translateX', value=translationsRotations[0], time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(control + '.translateY', value=translationsRotations[1], time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(control + '.translateZ', value=translationsRotations[2], time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(control + '.rotateX', value=translationsRotations[3], time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(control + '.rotateY', value=translationsRotations[4], time=frame, inTangentType="linear",
                     outTangentType="linear")
    cmds.setKeyframe(control + '.rotateZ', value=translationsRotations[5], time=frame, inTangentType="linear",
                     outTangentType="linear")


def horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                  translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                  translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                  translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame):
    # RIGHT FRONT LEG AND KNEE
    cmds.select("nurbsCircle2")
    rightFrontFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightFrontLeg, rightFrontFootControl, frame)
    cmds.select("nurbsCircle23")
    rightFrontKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightFrontKnee, rightFrontKneeControl, frame)
    # LEFT FRONT LEG AND KNEE 
    cmds.select("nurbsCircle1")
    leftFrontFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftFrontLeg, leftFrontFootControl, frame)
    cmds.select("nurbsCircle25")
    leftFrontKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftFrontKnee, leftFrontKneeControl, frame)
    # RIGHT BACK LEG AND KNEE
    cmds.select("nurbsCircle6")
    rightBackFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightBackLeg, rightBackFootControl, frame)
    cmds.select("nurbsCircle24")
    rightBackKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightBackKnee, rightBackKneeControl, frame)
    # LEFT BACK LEG AND KNEE
    cmds.select("nurbsCircle7")
    leftBackFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftBackLeg, leftBackFootControl, frame)
    cmds.select("nurbsCircle26")
    leftBackKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftBackKnee, leftBackKneeControl, frame)


def horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                   translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                   translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                   translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                   translationsRotationsBody, frame):
    # RIGHT FRONT LEG AND KNEE
    cmds.select("nurbsCircle2")
    rightFrontFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightFrontLeg, rightFrontFootControl, frame)
    cmds.select("nurbsCircle23")
    rightFrontKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightFrontKnee, rightFrontKneeControl, frame)
    # LEFT FRONT LEG AND KNEE 
    cmds.select("nurbsCircle1")
    leftFrontFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftFrontLeg, leftFrontFootControl, frame)
    cmds.select("nurbsCircle25")
    leftFrontKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftFrontKnee, leftFrontKneeControl, frame)
    # RIGHT BACK LEG AND KNEE
    cmds.select("nurbsCircle6")
    rightBackFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightBackLeg, rightBackFootControl, frame)
    cmds.select("nurbsCircle24")
    rightBackKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsRightBackKnee, rightBackKneeControl, frame)
    # LEFT BACK LEG AND KNEE
    cmds.select("nurbsCircle7")
    leftBackFootControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftBackLeg, leftBackFootControl, frame)
    cmds.select("nurbsCircle26")
    leftBackKneeControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsLeftBackKnee, leftBackKneeControl, frame)
    # BODY
    cmds.select("nurbsCircle21")
    bodyControl = cmds.ls(selection=True)[0]
    horseActionKeySetForBodySegment(translationsRotationsBody, bodyControl, frame)


def horseRun(nrOfAnimationRepetitions, startFrame):
    print("Run")
    frame = startFrame
    # FRAME 0
    translationsRotationsRightFrontLeg = [0, 0, 0, 0, 0,
                                          0]  # translateX, translateY, translateZ, rotateX, rotateY, rotateZ
    translationsRotationsRightFrontKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftFrontLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftFrontKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsRightBackLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsRightBackKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftBackLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftBackKnee = [0, 0, 0, 0, 0, 0]
    horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                  translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                  translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                  translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
    i = 0
    while i < nrOfAnimationRepetitions:
        # FRAME 1
        frame += 1
        translationsRotationsRightFrontLeg = [1.928, 1.834, 0, 0, 0, -31.274]
        translationsRotationsRightFrontKnee = [0, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [1.75, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-5.563, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [4.883, 0, 0, 0, 0, -31.384]
        translationsRotationsRightBackKnee = [0, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-1.726, 0.079, 0.214, 0, 0, -47.465]
        translationsRotationsLeftBackKnee = [-0.881, -5.252, 0, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 2
        frame += 1
        translationsRotationsRightFrontLeg = [2.356, 1.241, 0, 0, 0, -13.8]
        translationsRotationsRightFrontKnee = [0, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [0.831, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-5.563, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.012, -1.031, 0, 0, 0, 5.572]
        translationsRotationsRightBackKnee = [0.11, 1.126, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-6.541, 0.411, 0.214, 0, 0, -130.643]
        translationsRotationsLeftBackKnee = [-5.523, -0.992, 0, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 3
        frame += 1
        translationsRotationsRightFrontLeg = [3.542, 1.241, 0, 0, 0, 26.744]
        translationsRotationsRightFrontKnee = [1.089, -0.549, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.109, 0.449, 0, 0, 0, -42.623]
        translationsRotationsLeftFrontKnee = [-5.563, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.659, -1.031, 0, 0, 0, -5.327]
        translationsRotationsRightBackKnee = [0.11, 1.126, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-3.027, 2.627, 0.214, 0, 0, -105.97]
        translationsRotationsLeftBackKnee = [0.28, -5.739, 0, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 4
        frame += 1
        translationsRotationsRightFrontLeg = [2.859, -1.662, 0, 0, 0, -18.173]
        translationsRotationsRightFrontKnee = [1.089, -0.549, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.816, 1.408, 0, 0, 0, -66.467]
        translationsRotationsLeftFrontKnee = [-5.563, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-1.296, -1.031, 0, 0, 0, -5.327]
        translationsRotationsRightBackKnee = [2.85, 1.382, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-2.521, 2.198, 0.214, 0, 0, -70.998]
        translationsRotationsLeftBackKnee = [-3.017, -7.136, 0, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 5
        frame += 1
        translationsRotationsRightFrontLeg = [1.055, -2.674, 0, 0, 0, 0]
        translationsRotationsRightFrontKnee = [1.089, -0.549, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-2.102, 2.273, 0, 0, 0, -66.467]
        translationsRotationsLeftFrontKnee = [-3.017, -7.136, 0.614, 0, 0, 0]
        translationsRotationsRightBackLeg = [-4.903, -3.739, 0, 0, 0, -92.004]
        translationsRotationsRightBackKnee = [2.85, 1.382, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-1.042, 3.063, 0.214, 0, 0, -44.524]
        translationsRotationsLeftBackKnee = [-3.017, -7.136, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 6
        frame += 1
        translationsRotationsRightFrontLeg = [-1.329, -3.028, 0, 0, 0, 21.353]
        translationsRotationsRightFrontKnee = [1.089, -0.549, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.816, 3.18, 0, 0, 0, -66.467]
        translationsRotationsLeftFrontKnee = [-3.442, -0.924, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-3.012, 1.504, 0, 0, 0, -107.57]
        translationsRotationsRightBackKnee = [3.568, -0.886, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-0.197, 3.75, 0.214, 0, 0, -32.655]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 7
        frame += 1
        translationsRotationsRightFrontLeg = [-2.968, -4.166, 0, 0, 0, -83.684]
        translationsRotationsRightFrontKnee = [4.343, -1.821, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.308, 2.182, 0, 0, 0, -66.467]
        translationsRotationsLeftFrontKnee = [-3.442, -0.924, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-1.861, 1.383, 0, 0, 0, -103.665]
        translationsRotationsRightBackKnee = [3.568, -0.886, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [0.276, 2.507, 0.214, 0, 0, -32.655]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 8
        frame += 1
        translationsRotationsRightFrontLeg = [-2.094, 0.725, 0, 0, 0, -83.684]
        translationsRotationsRightFrontKnee = [1.414, 0.329, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.261, 1.578, 0, 0, 0, -66.467]
        translationsRotationsLeftFrontKnee = [-3.442, -0.924, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-0.602, 0.88, 0, 0, 0, -103.665]
        translationsRotationsRightBackKnee = [3.568, -0.886, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.732, 1.814, 0.214, 0, 0, -15.464]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 9
        frame += 1
        translationsRotationsRightFrontLeg = [-2.61, 1.258, 0, 0, 0, -112.914]
        translationsRotationsRightFrontKnee = [1.414, 0.329, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [1.342, 1.031, 0, 0, 0, -46.438]
        translationsRotationsLeftFrontKnee = [-3.442, -0.924, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [1.446, 1.046, 0, 0, 0, -45.196]
        translationsRotationsRightBackKnee = [-0.598, 3.139, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [3.133, 0.724, 0.214, 0, 0, -15.464]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 10
        frame += 1
        translationsRotationsRightFrontLeg = [-1.178, 1.435, 0, 0, 0, -129.008]
        translationsRotationsRightFrontKnee = [1.414, 0.329, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [3.058, 1.528, 0, 0, 0, -5.815]
        translationsRotationsLeftFrontKnee = [-6.577, -4.22, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [1.727, 1.859, 0, 0, 0, -45.196]
        translationsRotationsRightBackKnee = [-0.598, 3.139, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [4.137, 0.487, 0.214, 0, 0, -15.464]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 11
        frame += 1
        translationsRotationsRightFrontLeg = [0.104, 1.303, 0, 0, 0, -77.927]
        translationsRotationsRightFrontKnee = [-0.959, 3.258, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [4.452, 1.076, 0, 0, 0, -5.815]
        translationsRotationsLeftFrontKnee = [-6.577, -4.22, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.515, 2.291, 0, 0, 0, -45.196]
        translationsRotationsRightBackKnee = [-0.598, 3.139, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [2.723, -0.003, 0.214, 0, 0, -0.421]
        translationsRotationsLeftBackKnee = [-4.643, -4.599, 0.614, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)
        # FRAME 12
        frame += 1
        translationsRotationsRightFrontLeg = [0.73, 0.949, 0, 0, 0, -55.655]
        translationsRotationsRightFrontKnee = [-0.959, 3.258, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [3.487, -0.025, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-6.577, -4.22, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.932, 1.791, 0, 0, 0, -21.809]
        translationsRotationsRightBackKnee = [0.499, 0.397, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [0, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackKnee = [0, 0, 0, 0, 0, 0]
        horseRunFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                      translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                      translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                      translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee, frame)

        i += 1


def horseJump(nrOfAnimationRepetitions, startFrame):
    print("Jump")
    frame = startFrame
    # FRAME 0
    translationsRotationsRightFrontLeg = [0, 0, 0, 0, 0,
                                          0]  # translateX, translateY, translateZ, rotateX, rotateY, rotateZ
    translationsRotationsRightFrontKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftFrontLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftFrontKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsRightBackLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsRightBackKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftBackLeg = [0, 0, 0, 0, 0, 0]
    translationsRotationsLeftBackKnee = [0, 0, 0, 0, 0, 0]
    translationsRotationsBody = [0, 0, 0, 0, 0, 0]
    horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                   translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                   translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                   translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                   translationsRotationsBody, frame)
    i = 0
    while i < nrOfAnimationRepetitions:
        # FRAME 1
        frame += 1
        translationsRotationsRightFrontLeg = [-1.16, -0.62, 0, 0, 0, 0]
        translationsRotationsRightFrontKnee = [1.806, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.905, -0.032, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [1.977, -2.215, 0, 0, 0, -50.017]
        translationsRotationsRightBackKnee = [1.687, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [2.635, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 2
        frame += 1
        translationsRotationsRightFrontLeg = [-1.467, -0.62, 0, 0, 0, -30.892]
        translationsRotationsRightFrontKnee = [1.806, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.905, 0.382, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [1.383, -1.944, 0, 0, 0, -50.017]
        translationsRotationsRightBackKnee = [1.687, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [2.04, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 3
        frame += 1
        translationsRotationsRightFrontLeg = [-1.662, -0.62, 0, 0, 0, -37.879]
        translationsRotationsRightFrontKnee = [1.806, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [0.825, 1.032, 0, 0, 0, -28.512]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.855, -1.944, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.687, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.327, 1.08, 0, 0, 0, -28.512]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 4
        frame += 1
        translationsRotationsRightFrontLeg = [-2.542, -0.186, 0, 0, 0, -5.779]
        translationsRotationsRightFrontKnee = [1.806, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [1.85, 1.072, 0, 0, 0, -28.512]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.238, -2.023, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.687, 0, 0, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.905, 1.422, 0, 0, 0, -28.512]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 5
        frame += 1
        translationsRotationsRightFrontLeg = [-0.275, 1.798, 0, 0, 0, -88.944]
        translationsRotationsRightFrontKnee = [1.806, 0, -0.407, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [2.744, 0.002, 0, 0, 0, -0.578]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-0.878, 0.935, 0, 0, 0, -86.225]
        translationsRotationsRightBackKnee = [1.806, 0, -0.407, 0, 0, 0]
        translationsRotationsLeftBackLeg = [3.662, 0.543, 0, 0, 0, 19.69]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, -0.084, 0.137, 4.253]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 6
        frame += 1
        translationsRotationsRightFrontLeg = [1.323, 3.212, 0, 0, 0, -88.944]
        translationsRotationsRightFrontKnee = [1.806, 0, -0.407, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.697, 0.002, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-2.198, -1.676, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.392, 3.059, 0, 0, 0, -86.225]
        translationsRotationsRightBackKnee = [1.687, 0, 0.484, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.27, -0.018, 0, 0, 0, 0]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, -0.084, 0.137, 20.593]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 7
        frame += 1
        translationsRotationsRightFrontLeg = [0.855, 2.61, 0, 0, 0, -88.944]
        translationsRotationsRightFrontKnee = [1.806, 0, -0.407, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.976, 0.3, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.044, 2.564, 0, 0, 0, -86.225]
        translationsRotationsRightBackKnee = [1.687, 0, 0.484, 0, 0, 0]
        translationsRotationsLeftBackLeg = [0.714, -0.018, 0, 0, 0, 0]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, -0.055, 0.244, 9.962]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 8
        frame += 1
        translationsRotationsRightFrontLeg = [0.261, 2.72, -0.082, 0, 0, -88.944]
        translationsRotationsRightFrontKnee = [1.764, 0.023, -0.694, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.747, 1.056, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [1.674, 2.607, 0, 0, 0, -86.225]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-2.153, 2.063, 0, 0, 0, -74.836]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, -0.055, 0.244, 9.962]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 9
        frame += 1
        translationsRotationsRightFrontLeg = [0.598, 2.502, -0.082, 0, 0, -72.548]
        translationsRotationsRightFrontKnee = [1.764, 0.023, -0.627, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.529, 2.186, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.051, 2.707, 0, 0, 0, -39.031]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-1.777, 2.341, 0, 0, 0, -74.836]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 10
        frame += 1
        translationsRotationsRightFrontLeg = [1.371, 1.696, -0.082, 0, 0, -72.548]
        translationsRotationsRightFrontKnee = [1.625, 0.069, -0.254, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.4, 3.491, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.308, 1.627, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-1.728, 3.968, 0, 0, 0, -74.836]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, -7.03]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 11
        frame += 1
        translationsRotationsRightFrontLeg = [2.257, 0.12, -0.082, 0, 0, 24.018]
        translationsRotationsRightFrontKnee = [1.625, 0.069, -0.254, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-0.724, 4.182, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [0.537, -0.024, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [-0.963, 4.223, 0, 0, 0, -74.836]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, -17.129]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 12
        frame += 1
        translationsRotationsRightFrontLeg = [0.173, -0.063, -0.082, 0, 0, 0]
        translationsRotationsRightFrontKnee = [1.625, 0.069, 0.049, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [0.396, 2.435, 0, 0, 0, -68.082]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-2.15, -0.042, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [0.784, 2.394, 0, 0, 0, -74.836]
        translationsRotationsLeftBackKnee = [-5.528, 0, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, -8.053]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 13
        frame += 1
        translationsRotationsRightFrontLeg = [-0.849, 0.613, -0.082, 0, 0, -124.285]
        translationsRotationsRightFrontKnee = [1.625, 0.069, -0.208, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [1.088, 0.985, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-2.101, -0.735, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.542, 1.504, 0, 0, 0, -25.173]
        translationsRotationsLeftBackKnee = [-6.889, -5.021, 0, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, -4.199]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 14
        frame += 1
        translationsRotationsRightFrontLeg = [0.255, 0.269, -0.082, 0, 0, -76.735]
        translationsRotationsRightFrontKnee = [-2.138, 1.797, -0.208, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [1.541, -0.029, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [-1.729, -4.074, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-2.264, -0.029, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [2.194, 0.599, 0, 0, 0, -1.951]
        translationsRotationsLeftBackKnee = [-6.889, -5.021, 0, 0, 0, 0]
        translationsRotationsBody = [0, -0.4, 0, 0, 0, -4.199]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 15
        frame += 1
        translationsRotationsRightFrontLeg = [1.219, 1.137, -0.082, 0, 0, -40.154]
        translationsRotationsRightFrontKnee = [1.159, -0.022, -0.11, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [0, 0, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [0, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [-0.496, 0.935, 0, 0, 0, -92.266]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [1.728, 0.181, 0, 0, 0, -1.951]
        translationsRotationsLeftBackKnee = [-4.492, -0.686, -0.456, 0, 0, 0]
        translationsRotationsBody = [0, 0, 0, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        # FRAME 16
        frame += 1
        translationsRotationsRightFrontLeg = [0.281, 0.753, -0.082, 0, 0, -87.254]
        translationsRotationsRightFrontKnee = [1.159, -0.022, -0.11, 0, 0, 0]
        translationsRotationsLeftFrontLeg = [-1.468, -0.569, 0, 0, 0, 0]
        translationsRotationsLeftFrontKnee = [0, 0, 0, 0, 0, 0]
        translationsRotationsRightBackLeg = [2.744, -2.251, 0, 0, 0, 0]
        translationsRotationsRightBackKnee = [1.857, 0.002, 0.211, 0, 0, 0]
        translationsRotationsLeftBackLeg = [2.997, -0.044, 0, 0, 0, -1.951]
        translationsRotationsLeftBackKnee = [-4.492, -0.686, -0.456, 0, 0, 0]
        horseJumpFrame(translationsRotationsRightFrontLeg, translationsRotationsRightFrontKnee,
                       translationsRotationsLeftFrontLeg, translationsRotationsLeftFrontKnee,
                       translationsRotationsRightBackLeg, translationsRotationsRightBackKnee,
                       translationsRotationsLeftBackLeg, translationsRotationsLeftBackKnee,
                       translationsRotationsBody, frame)
        i += 1
    return frame

# horseWalk(20, 0)
# horseRun(80, 166)
# horseJump(1, 0)
