import json
import math
import os
import random
import sys

import maya.cmds as cmds

os.chdir("C:\Users\Bidi\eclipse-workspace\Manhattan")  # change the current working directory to eclipse workspace
sys.path.append(r'C:\Users\Bidi\eclipse-workspace\Animations')
sys.path.append(r'C:\Users\Bidi\eclipse-workspace\Collision')

import horse_movements
import collision

cmds.warning('Hello World!')

horseXDisplacement = 4.713
horseZDisplacement = 4.881

listOfPathsToObjects = [r"C:\Users\Bidi\eclipse-workspace\Collision\fence\fence.mb",
                        r"C:\Users\Bidi\eclipse-workspace\Collision\pillar\pillar.mb"]
listOfIndexes = [-1 for i in range(0, len(listOfPathsToObjects)) if i >= 0]
listOfObjectNames = []
avoidedObjects = {}


# listOfObjectNames = ["pillar", "pillar_pillar", "pillar_pillar1", "pillar_pillar2", "pillar_pillar3", "pillar_pillar4", "fence", "fence_fence", "fence_fence1", "fence_fence2", "fence_fence3", "fence_fence4"]
# avoidedObjects = {"pillar":0, "pillar_pillar":0, "pillar_pillar1":0, "pillar_pillar2":0, "pillar_pillar3":0, "pillar_pillar4":0, "fence":0, "fence_fence":0, "fence_fence1":0, "fence_fence2":0, "fence_fence3":0, "fence_fence4":0}


# a list has tuples of a certain number of elements; it sorts it by the first element of the tuples
def maxListOfTuplesOrderByFirstElement(_list):
    _max = _list[0]
    for elem in _list:
        if elem[0] >= _max[0]:
            _max = elem
    return _max


# generates a random directed acyclic graph
def generateRandomDAG(filename, nRange, mUpperRange, weightsRange):
    # verifies if a graph has cycles or not using it's topological sorting
    def hasCycles(n, m, source, sink, listOfEdges):
        G = Graph(filename="", n=n, m=m, source=source, sink=sink, edges=listOfEdges)
        if G.TopologicalSorting() != (False, False):
            return False
        return True

    # normalizes a list (unites duplicate edges adding their weights together and removes edges going out from the sink or in the source)
    def normalizeList(_list, weightsRange, source,
                      sink):
        js = [(pair[0], pair[1]) for pair in _list]
        uniqueJs = list(set(js))
        duplicateJs = [j for j in uniqueJs if js.count(j) > 1]
        newListPairs = []
        for j in duplicateJs:
            duplicatePairs = [pair for pair in _list if pair[0] == j[0] and pair[1] == j[1]]
            newListPairs.append((j[0], j[1], sum([pair[2] for pair in duplicatePairs])))
            for duplicatePair in duplicatePairs:
                _list.remove(duplicatePair)
        for newPair in newListPairs:
            if newPair[2] > weightsRange[1]:
                _list.append((newPair[0], newPair[1], weightsRange[1]))
            elif newPair[2] < weightsRange[0]:
                _list.append((newPair[0], newPair[1], weightsRange[0]))
            else:
                _list.append(newPair)

        for pair in _list:
            if pair[0] == sink:
                _list.remove(pair)
            if pair[1] == source:
                _list.remove(pair)

        return _list

    cwd = os.getcwd()  # get current working directory
    f = open(cwd + '\\' + filename, "w+")  # the file in which we'll write the new graph

    n = random.randint(nRange[0], nRange[1])
    upperM = random.randint(mUpperRange[0], mUpperRange[
        1])  # a superior limit for the number of edges (including duplicates and those not satisfying source/sink constraints)
    source = random.randint(1, n)
    sink = source
    while sink == source:
        sink = random.randint(1, n)

    nodesWithoutSource = [i for i in range(1, n + 1) if i != source]
    nodesWithoutSink = [i for i in range(1, n + 1) if i != sink]
    listOfEdges = []
    while len(listOfEdges) < upperM:
        w = random.randint(weightsRange[0], weightsRange[1])
        x = random.choice(nodesWithoutSink)
        nodesWithoutSourceWithoutX = [i for i in nodesWithoutSource if i != x]
        y = random.choice(nodesWithoutSourceWithoutX)
        listOfEdges.append((x, y, w))
        while hasCycles(n, upperM, source, sink, listOfEdges) == True:  # here we assure there will be no cycles
            listOfEdges = listOfEdges[:-1]
            x = random.choice(nodesWithoutSink)
            nodesWithoutSourceWithoutX = [i for i in nodesWithoutSource if i != x]
            y = random.choice(nodesWithoutSourceWithoutX)
            listOfEdges.append((x, y, w))

    listOfEdges = normalizeList(listOfEdges, weightsRange, source,
                                sink)  # normalizing the list using the function above
    m = len(listOfEdges)  # the real number of edges

    # write the graph into the file
    f.write(str(n) + " " + str(m) + "\n\n")
    f.write(str(source) + " " + str(sink) + "\n\n")
    for i in range(0, m):
        if i != m - 1:
            f.write(str(listOfEdges[i][0]) + " " + str(listOfEdges[i][1]) + " " + str(listOfEdges[i][2]) + "\n")
        else:
            f.write(str(listOfEdges[i][0]) + " " + str(listOfEdges[i][1]) + " " + str(listOfEdges[i][2]))

    f.close()
    G = Graph(filename)
    return G


class Graph:
    def __init__(self, filename="", n="", m="", source="", sink="", edges=""):
        self.filename = filename  # the source file for the graph
        if filename == "" and (n == "" or m == "" or source == "" or sink == "" or edges == ""):
            self.n = 0  # the number of nodes
            self.m = 0  # the number of edges
            self.source = 0  # the label of the node who has no predecessors
            self.sink = 0  # the label of the node who has no successors
            self.edges = []  # the edges with the associated weights
        if n != "" and m != "" and source != "" and sink != "" and edges != "":
            self.n = n
            self.m = m
            self.source = source
            self.sink = sink
            self.edges = edges
        if filename != "" and (n == "" or m == "" or source == "" or sink == "" or edges == ""):
            f = open(filename, "r")
            string = f.readline().split("\n")[0]
            self.n = int(string.split(" ")[0])
            self.m = int(string.split(" ")[1])
            f.readline()
            string = f.readline().split("\n")[0]
            self.source = int(string.split(" ")[0])
            self.sink = int(string.split(" ")[1])
            f.readline()
            self.edges = []
            i = 0
            while i < self.m:
                string = f.readline().split("\n")[0]
                self.edges.append((int(string.split(" ")[0]), int(string.split(" ")[1]), float(string.split(" ")[2])))
                i += 1
            f.close()

    # returns the number of vertices which enter the vertex given as parameter
    def inDegree(self, vertex):
        return len([edge[0] for edge in self.edges if edge[1] == vertex])

    # returns the number of vertices that leave the vertex given as parameter
    def outDegree(self, vertex):
        return len([edge[1] for edge in self.edges if edge[0] == vertex])

    # returns the vertices which enter the vertex given as parameter
    # and the associated weights on the corresponding edges
    def inNodesWithWeights(self, vertex):
        return [(edge[0], edge[2]) for edge in self.edges if edge[1] == vertex]

    # returns the vertices that leave the vertex given as parameter
    # and the associated weights on the corresponding edges
    def outNodesWithWeights(self, vertex):
        return [(edge[1], edge[2]) for edge in self.edges if edge[0] == vertex]

    # returns the topological order of the vertices or false if the graph isn't acyclic
    def TopologicalSorting(self):
        dG_ = {i: self.inDegree(i) for i in range(1, self.n + 1)}  # the in degree of every vertex
        s = [i for i in dG_.keys() if dG_[i] == 0]  # stack
        order = {i: 0 for i in range(1, self.n + 1)}
        count = 0
        while len(s) != 0:
            v = s.pop(0)
            count += 1
            order[v] = count
            for w in [pair[0] for pair in self.outNodesWithWeights(v)]:
                dG_[w] -= 1
                if dG_[w] == 0:
                    s.append(w)
        if count == self.n:
            return True, order
        else:
            return False, False

    # return the longest path from source to sink using dynamic programming
    def Manhattan(self):
        longestPathVertexes = []
        maxWeight = 0

        distance = {i: -float('inf') for i in range(1, self.n + 1)}
        maxPredecessors = {i: -float('inf') for i in range(1, self.n + 1)}
        distance[self.source] = 0

        ok, order = self.TopologicalSorting()
        
        if ok == True:
            orderTuples = sorted(order.items(), key=lambda element: element[1])
            for v in [v[0] for v in orderTuples if v[1] > order[self.source]]:
                myList = [(distance[u[0]] + u[1], u[0]) for u in self.inNodesWithWeights(v)]
                if len(myList) == 0:
                    distance[v] = -float('inf')
                    maxPredecessors[v] = -float('inf')
                else:
                    distance[v] = maxListOfTuplesOrderByFirstElement(myList)[0]
                    maxPredecessors[v] = maxListOfTuplesOrderByFirstElement(myList)[1]
            maxWeight = distance[self.sink]

            longestPathVertexes.append(self.sink)
            value = maxPredecessors[self.sink]
            while value != -float('inf'):
                longestPathVertexes.append(value)
                value = maxPredecessors[longestPathVertexes[len(longestPathVertexes) - 1]]
            longestPathVertexes.reverse()

            longestPathEdges = [(longestPathVertexes[i], longestPathVertexes[i + 1]) for i in
                                range(0, len(longestPathVertexes) - 1)]

            return [v for v in order.values()], longestPathEdges, maxWeight
        else:
            return "The graph has cycles!", "The graph has cycles!", "The graph has cycles!"


def drawGraphInMaya(graph):
    # get the topological sorting of the graph
    order = graph.TopologicalSorting()[1]

    # draw the ground - plane
    planeDimension = 100 * (graph.n - 1)
    plane = cmds.polyPlane(n="ground", sx=100, sy=100, sh=1, sw=1, h=planeDimension, w=planeDimension)
    cmds.setAttr(plane[0] + ".translateX", cmds.polyPlane(plane[0], query=True, width=True) / 2)
    heightUnit = (cmds.polyPlane(plane[0], query=True, height=True) / 2) / graph.n
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)  # freeze transformations

    # assign material - texture to the ground
    _file = "C:\Users\Bidi\eclipse-workspace\\grass.png"
    shader = cmds.shadingNode("lambert", asTexture=True, n="groundTexture")
    fileNode = cmds.shadingNode("file", asTexture=True, n="groundFileNode")
    shadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
    cmds.setAttr(fileNode + ".fileTextureName", _file, type="string")
    cmds.connectAttr(shader + ".outColor", shadingGroup + ".surfaceShader", force=True)
    cmds.connectAttr(fileNode + ".outColor", shader + ".color", force=True)
    cmds.surfaceShaderList(shader, add=shadingGroup)
    cmds.sets(plane[0], e=True, forceElement=shadingGroup)
    
    orderTuples = sorted(order.items(), key=lambda element: element[1])
    
    # draw the nodes of the graph - space locators
    for i in range(0, graph.n):
        locator = cmds.spaceLocator(n="node" + str(orderTuples[i][0]))
        cmds.setAttr(locator[0] + ".scale",
                     cmds.getAttr(locator[0] + ".scaleX") * 10,
                     cmds.getAttr(locator[0] + ".scaleY") * 10,
                     cmds.getAttr(locator[0] + ".scaleZ") * 10)
        cmds.move(100 * i, 0, 0, locator)

    # draw the edges of the graph - curves with degree 1
    curves = []  # the curves represented by the graph edges and the coordinates of the points forming them

    edgesHeightsPositions = []  # the height of an edge over the field (all the possible Z's)

    i = 1
    while i * heightUnit <= heightUnit * graph.n:
        edgesHeightsPositions.append(i * heightUnit)
        i += 1
    edgesHeightsPositions += [-i for i in edgesHeightsPositions]

    for edge in graph.edges:
        beginVertexOrder = order[edge[0]]
        endVertexOrder = order[edge[1]]
        if endVertexOrder == beginVertexOrder + 1:  # the nodes are one after the other, so we'll draw a straight line
            # 2 points form the line
            curvePoint1 = (cmds.getAttr("node" + str(edge[0]) + ".translateX"), 0, 0)
            curvePoint2 = (cmds.getAttr("node" + str(edge[1]) + ".translateX"), 0, 0)
            curves.append((edge, [curvePoint1, curvePoint2]))
            cmds.curve(d=1, p=curves[-1][1], n="edge_" + str(edge[0]) + "_" + str(edge[1]))
            
        else:  # the nodes are distant so we'll draw a rectangular line passing a certain height
            edgeHeightPosition = random.choice(edgesHeightsPositions)
            edgesHeightsPositions.remove(edgeHeightPosition)

            # 4 points form the line
            curvePoint1 = (cmds.getAttr("node" + str(edge[0]) + ".translateX"), 0, 0)
            curvePoint2 = (cmds.getAttr("node" + str(edge[0]) + ".translateX"), 0, edgeHeightPosition)
            curvePoint3 = (cmds.getAttr("node" + str(edge[1]) + ".translateX"), 0, edgeHeightPosition)
            curvePoint4 = (cmds.getAttr("node" + str(edge[1]) + ".translateX"), 0, 0)
            curves.append((edge, [curvePoint1, curvePoint2, curvePoint3, curvePoint4]))
            cmds.curve(d=1, p=curves[-1][1], n="edge_" + str(edge[0]) + "_" + str(edge[1]))
            
    return planeDimension, curves


def graphTraversalAnimation(pathToObject, objectName, controlName, curves, longestPath):
    # brings the object that will traverse the graph into the scene and sets it in position at the source
    cmds.file(pathToObject, i=True)
    # cmds.setAttr(objectName + ".translate", 0, 0, 0)
    # cmds.setAttr(objectName + ".rotate", 0, 0, 0)

    objectBoundingBox = cmds.xform(objectName, q=True, bb=True)
    objectBoundingBoxWidth = abs(objectBoundingBox[3] - objectBoundingBox[0])
    objectBoundingBoxHeight = abs(objectBoundingBox[4] - objectBoundingBox[1])
    objectBoundingBoxDepth = abs(objectBoundingBox[5] - objectBoundingBox[2])
    cmds.xform(objectName, t=[objectBoundingBoxWidth / 2, objectBoundingBoxHeight / 2, objectBoundingBoxDepth * 0])

    currentFrame = 0
    for i in range(0, len(longestPath)):
        polygonalLine = \
            [curve[1] for curve in curves if curve[0][0] == longestPath[i][0] and curve[0][1] == longestPath[i][1]][0]

        if i == 0:
            cmds.setKeyframe(controlName + '.translateX',
                             value=polygonalLine[0][0] + objectBoundingBoxWidth / 2 - horseXDisplacement,
                             time=currentFrame, inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(controlName + '.translateZ', value=polygonalLine[0][2] - horseZDisplacement,
                             time=currentFrame,
                             inTangentType="linear", outTangentType="linear")

            # key frames for horse orientation
            if polygonalLine[0][0] < polygonalLine[1][0]:
                cmds.setKeyframe(controlName + '.rotateY', value=0, time=currentFrame,
                                 inTangentType="linear", outTangentType="linear")
            elif polygonalLine[0][0] > polygonalLine[1][0]:
                cmds.setKeyframe(controlName + '.rotateY', value=180, time=currentFrame,
                                 inTangentType="linear", outTangentType="linear")
            else:
                if polygonalLine[0][2] == 0 and polygonalLine[1][2] > 0:
                    cmds.setKeyframe(controlName + '.rotateY', value=-90, time=currentFrame,
                                     inTangentType="linear", outTangentType="linear")
                if polygonalLine[0][2] == 0 and polygonalLine[1][2] < 0:
                    cmds.setKeyframe(controlName + '.rotateY', value=90, time=currentFrame,
                                     inTangentType="linear", outTangentType="linear")

            # 1 frame at 3 units of path
            edgeDimension = abs(polygonalLine[1][2]) if polygonalLine[0][0] == polygonalLine[1][0] else abs(
                polygonalLine[0][0] - polygonalLine[1][0])
            currentFrame += math.ceil(edgeDimension / 3)

        for j in range(1, len(polygonalLine)):
            cmds.setKeyframe(controlName + '.translateX', value=polygonalLine[j][0], time=currentFrame,
                             inTangentType="linear", outTangentType="linear")
            cmds.setKeyframe(controlName + '.translateZ', value=polygonalLine[j][2] - horseZDisplacement,
                             time=currentFrame,
                             inTangentType="linear", outTangentType="linear")

            # key frames for horse orientation
            if j < len(polygonalLine) - 1:
                if polygonalLine[j][0] < polygonalLine[j + 1][0]:
                    aroundTheCorner(controlName, 0, currentFrame)
                if polygonalLine[j][0] > polygonalLine[j + 1][0]:
                    aroundTheCorner(controlName, 180, currentFrame)
                if polygonalLine[j][0] == polygonalLine[j + 1][0]:
                    if polygonalLine[j][2] == 0 and polygonalLine[j + 1][2] > 0:
                        aroundTheCorner(controlName, -90, currentFrame)
                    if polygonalLine[j][2] == 0 and polygonalLine[j + 1][2] < 0:
                        aroundTheCorner(controlName, 90, currentFrame)
                    if polygonalLine[j][2] > 0 and polygonalLine[j + 1][2] == 0:
                        aroundTheCorner(controlName, 90, currentFrame)
                    if polygonalLine[j][2] < 0 and polygonalLine[j + 1][2] == 0:
                        aroundTheCorner(controlName, -90, currentFrame)
            if j == len(polygonalLine) - 1 and i < len(longestPath) - 1:
                newPolygonalLine = \
                    [curve[1] for curve in curves if
                     curve[0][0] == longestPath[i + 1][0] and curve[0][1] == longestPath[i + 1][1]][0]
                if polygonalLine[j][0] < newPolygonalLine[1][0]:
                    aroundTheCorner(controlName, 0, currentFrame)
                elif polygonalLine[j][0] > newPolygonalLine[1][0]:
                    aroundTheCorner(controlName, 180, currentFrame)
                else:
                    if polygonalLine[j][2] == 0 and newPolygonalLine[1][2] > 0:
                        aroundTheCorner(controlName, -90, currentFrame)
                    if polygonalLine[j][2] == 0 and newPolygonalLine[1][2] < 0:
                        aroundTheCorner(controlName, 90, currentFrame)
                    if polygonalLine[j][2] > 0 and newPolygonalLine[1][2] == 0:
                        aroundTheCorner(controlName, 90, currentFrame)
                    if polygonalLine[j][2] < 0 and newPolygonalLine[1][2] == 0:
                        aroundTheCorner(controlName, -90, currentFrame)

            # 1 frame at 3 units of path
            edgeDimension = 0
            if j < len(polygonalLine) - 1:
                if polygonalLine[j][2] == polygonalLine[j + 1][2]:
                    edgeDimension = abs(polygonalLine[j][0] - polygonalLine[j + 1][0])
                if polygonalLine[j][0] == polygonalLine[j + 1][0]:
                    edgeDimension = max(abs(polygonalLine[j][2]), abs(polygonalLine[j + 1][2]))
            if j == len(polygonalLine) - 1 and i < len(longestPath) - 1:
                newPolygonalLine = \
                    [curve[1] for curve in curves if
                     curve[0][0] == longestPath[i + 1][0] and curve[0][1] == longestPath[i + 1][1]][0]
                if polygonalLine[j][2] == newPolygonalLine[1][2]:
                    edgeDimension = abs(polygonalLine[j][0] - newPolygonalLine[1][0])
                if polygonalLine[j][0] == newPolygonalLine[1][0]:
                    edgeDimension = max(abs(polygonalLine[j][2]), abs(newPolygonalLine[1][2]))
            currentFrame += math.ceil(edgeDimension / 3)


def aroundTheCorner(controlName, value, currentFrame):
    currentValue = cmds.getAttr(controlName + ".rotateY")
    allValues = [currentValue]

    if value == 0:
        if currentValue == 90:
            allValues.append(90 - 90 * 1.0 / 4)
            allValues.append(90 - 2 * (90 * 1.0 / 4))
            allValues.append(90 - 3 * (90 * 1.0 / 4))
        if currentValue == -90:
            allValues.append(-90 + 90 * 1.0 / 4)
            allValues.append(-90 + 2 * (90 * 1.0 / 4))
            allValues.append(-90 + 3 * (90 * 1.0 / 4))
        if currentValue == 180:
            allValues.append(180 - 180 * 1.0 / 4)
            allValues.append(180 - 2 * (180 * 1.0 / 4))
            allValues.append(180 - 3 * (180 * 1.0 / 4))
        allValues.append(0)
        cmds.setAttr(controlName + ".rotateY", 0)
    if value == 90:
        if currentValue == 0:
            allValues.append(90 * 1.0 / 4)
            allValues.append(2 * (90 * 1.0 / 4))
            allValues.append(3 * (90 * 1.0 / 4))
        if currentValue == 180:
            allValues.append(180 - 90 * 1.0 / 4)
            allValues.append(180 - 2 * (90 * 1.0 / 4))
            allValues.append(180 - 3 * (90 * 1.0 / 4))
        if currentValue == -90:
            allValues.append(-90 + 180 * 1.0 / 4)
            allValues.append(-90 + 2 * (180 * 1.0 / 4))
            allValues.append(-90 + 3 * (180 * 1.0 / 4))
        allValues.append(90)
        cmds.setAttr(controlName + ".rotateY", 90)
    if value == -90:
        if currentValue == 0:
            allValues.append(-90 * 1.0 / 4)
            allValues.append(-2 * (90 * 1.0 / 4))
            allValues.append(-3 * (90 * 1.0 / 4))
        if currentValue == 180:
            allValues.append(-90 - 3 * (90 * 1.0 / 4))
            allValues.append(-90 - 2 * (90 * 1.0 / 4))
            allValues.append(-90 - (90 * 1.0 / 4))
        if currentValue == 90:
            allValues.append(90 - 180 * 1.0 / 4)
            allValues.append(90 - 2 * (180 * 1.0 / 4))
            allValues.append(90 - 3 * (180 * 1.0 / 4))
        allValues.append(-90)
        cmds.setAttr(controlName + ".rotateY", -90)
    if value == 180:
        if currentValue == 90:
            allValues.append(90 + 90 * 1.0 / 4)
            allValues.append(90 + 2 * (90 * 1.0 / 4))
            allValues.append(90 + 3 * (90 * 1.0 / 4))
        if currentValue == -90:
            allValues.append(-90 - (90 * 1.0 / 4))
            allValues.append(-90 - 2 * (90 * 1.0 / 4))
            allValues.append(-90 - 3 * (90 * 1.0 / 4))
        if currentValue == 0:
            allValues.append((180 * 1.0 / 4))
            allValues.append(2 * (180 * 1.0 / 4))
            allValues.append(3 * (180 * 1.0 / 4))
        allValues.append(180)
        cmds.setAttr(controlName + ".rotateY", 180)

    if len(allValues) == 5:
        cmds.setKeyframe(controlName + '.rotateY', value=allValues[0], time=currentFrame - 2,
                         inTangentType="linear", outTangentType="linear")
        cmds.setKeyframe(controlName + '.rotateY', value=allValues[1], time=currentFrame - 1,
                         inTangentType="linear", outTangentType="linear")
        cmds.setKeyframe(controlName + '.rotateY', value=allValues[2], time=currentFrame,
                         inTangentType="linear", outTangentType="linear")
        cmds.setKeyframe(controlName + '.rotateY', value=allValues[3], time=currentFrame + 1,
                         inTangentType="linear", outTangentType="linear")
        cmds.setKeyframe(controlName + '.rotateY', value=allValues[4], time=currentFrame + 2,
                         inTangentType="linear", outTangentType="linear")
    currentFrame -= 2


def serializeResults(fileName, planeDimension, longestPath, curves):
    longestPathList = []
    curvesList = []
    for elem in longestPath:
        longestPathList.append(elem[0])
        longestPathList.append(elem[1])
    for curve in curves:
        if len(curve[1]) == 2:
            curvesList.append(2.0)
        else:
            curvesList.append(4.0)
        curvesList.append(curve[0][0] * 1.0)
        curvesList.append(curve[0][1] * 1.0)
        curvesList.append(curve[0][2] * 1.0)
        for elem in curve[1]:
            curvesList.append(elem[0] * 1.0)
            curvesList.append(elem[1] * 1.0)
            curvesList.append(elem[2] * 1.0)
    d = {"planeDimension": planeDimension, "longestPath": longestPathList, "curves": curvesList};
    s = json.dumps(d)
    open(fileName, "wt").write(s)


def placeObstaclesOnMap(curves):
    for curve in curves:
        if len(curve[1]) == 2:
            minimum = int(min(curve[1][0][0], curve[1][1][0]))
            maximum = int(max(curve[1][0][0], curve[1][1][0]))
            possiblePositions = [i for i in range(minimum + 30, maximum - 29)]
            for i in range(0, int(curve[0][2])):
                if len(possiblePositions) > 1:
                    randomPosition = random.choice(possiblePositions)
                    for i in range(randomPosition - 40, randomPosition + 41):
                        if i in possiblePositions:
                            possiblePositions.remove(i)
                    
                    randomIndex = random.randint(0, len(listOfPathsToObjects) - 1)
                    pathToNewObject = listOfPathsToObjects[randomIndex]

                    cmds.file(pathToNewObject, i=True)
                    objectName = pathToNewObject.split("\\")[-1].split(".mb")[0]
                    if listOfIndexes[randomIndex] == 0:
                        objectName += "_" + objectName
                    if listOfIndexes[randomIndex] > 0:
                        objectName += "_" + objectName + str(listOfIndexes[randomIndex])
                    listOfIndexes[randomIndex] += 1
                    listOfObjectNames.append(objectName)
                    avoidedObjects[objectName] = 0

                    cmds.setAttr(objectName + ".translateX", randomPosition)
        if len(curve[1]) == 4:
            minimum = int(min(curve[1][0][2], curve[1][1][2]))
            maximum = int(max(curve[1][0][2], curve[1][1][2]))
            possiblePositions1 = [i for i in range(minimum + 30, maximum - 29)]

            minimum = int(min(curve[1][1][0], curve[1][2][0]))
            maximum = int(max(curve[1][1][0], curve[1][2][0]))
            possiblePositions2 = [i for i in range(minimum + 30, maximum - 29)]

            minimum = int(min(curve[1][2][2], curve[1][3][2]))
            maximum = int(max(curve[1][2][2], curve[1][3][2]))
            possiblePositions3 = [i for i in range(minimum + 30, maximum - 29)]

            for i in range(0, int(curve[0][2])):
                randomEdgeSection = random.randint(0, 2)
                if randomEdgeSection == 0:
                    if len(possiblePositions1) > 1:
                        randomPosition = random.choice(possiblePositions1)
                        for i in range(randomPosition - 40, randomPosition + 41):
                            if i in possiblePositions1:
                                possiblePositions1.remove(i)
                        
                        randomIndex = random.randint(0, len(listOfPathsToObjects) - 1)
                        pathToNewObject = listOfPathsToObjects[randomIndex]

                        cmds.file(pathToNewObject, i=True)
                        objectName = pathToNewObject.split("\\")[-1].split(".mb")[0]
                        if listOfIndexes[randomIndex] == 0:
                            objectName += "_" + objectName
                        if listOfIndexes[randomIndex] > 0:
                            objectName += "_" + objectName + str(listOfIndexes[randomIndex])
                        listOfIndexes[randomIndex] += 1
                        listOfObjectNames.append(objectName)
                        avoidedObjects[objectName] = 0

                        cmds.setAttr(objectName + ".translateX", curve[1][0][0])
                        cmds.setAttr(objectName + ".rotateY", 90)
                        cmds.setAttr(objectName + ".translateZ", randomPosition)
                elif randomEdgeSection == 1:
                    if len(possiblePositions2) > 1:
                        randomPosition = random.choice(possiblePositions2)
                        for i in range(randomPosition - 40, randomPosition + 41):
                            if i in possiblePositions2:
                                possiblePositions2.remove(i)      
                                 
                        randomIndex = random.randint(0, len(listOfPathsToObjects) - 1)
                        pathToNewObject = listOfPathsToObjects[randomIndex]

                        cmds.file(pathToNewObject, i=True)
                        objectName = pathToNewObject.split("\\")[-1].split(".mb")[0]
                        if listOfIndexes[randomIndex] == 0:
                            objectName += "_" + objectName
                        if listOfIndexes[randomIndex] > 0:
                            objectName += "_" + objectName + str(listOfIndexes[randomIndex])
                        listOfIndexes[randomIndex] += 1
                        listOfObjectNames.append(objectName)
                        avoidedObjects[objectName] = 0

                        cmds.setAttr(objectName + ".translateX", randomPosition)
                        cmds.setAttr(objectName + ".translateZ", curve[1][1][2])
                else:
                    if len(possiblePositions3) > 1:
                        randomPosition = random.choice(possiblePositions3)
                        for i in range(randomPosition - 40, randomPosition + 41):
                            if i in possiblePositions3:
                                possiblePositions3.remove(i)
                                
                        randomIndex = random.randint(0, len(listOfPathsToObjects) - 1)
                        pathToNewObject = listOfPathsToObjects[randomIndex]

                        cmds.file(pathToNewObject, i=True)
                        objectName = pathToNewObject.split("\\")[-1].split(".mb")[0]
                        if listOfIndexes[randomIndex] == 0:
                            objectName += "_" + objectName
                        if listOfIndexes[randomIndex] > 0:
                            objectName += "_" + objectName + str(listOfIndexes[randomIndex])
                        listOfIndexes[randomIndex] += 1
                        listOfObjectNames.append(objectName)
                        avoidedObjects[objectName] = 0

                        cmds.setAttr(objectName + ".translateX", curve[1][3][0])
                        cmds.setAttr(objectName + ".rotateY", 90)
                        cmds.setAttr(objectName + ".translateZ", randomPosition)


def completeAnimation(myObjectName, myObjectControlName, maxFrame):
    for i in range(0, maxFrame):
        cmds.currentTime(i, update=1)
        for objectName in listOfObjectNames:
            # Z from negative to positive
            orientation = cmds.xform(myObjectControlName, q=1, rotation=1, worldSpace=1)[1]
            if -91 <= orientation <= -89:
                if avoidedObjects[objectName] == 0 and collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                objectName, "Z", 1):
                    horse_movements.horseJump(1, i - 5)
                    collision.objectJump(myObjectName, myObjectControlName, objectName, "Z", 1, i, i + 10)
                    avoidedObjects[objectName] = 1
                elif avoidedObjects[objectName] == 0 and not collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                      objectName, "Z", 1) and \
                        collision.boxesCollisionNoRotations(myObjectName, myObjectControlName, objectName, 0,
                                                            collision.constraints[0][1], 1):
                    collision.objectDodge(myObjectName, myObjectControlName, objectName, "Z", 1, i, i + 15)
                    avoidedObjects[objectName] = 1
            # Z from positive to negative
            elif 89 <= orientation <= 91:
                if avoidedObjects[objectName] == 0 and collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                objectName, "Z", -1):
                    horse_movements.horseJump(1, i - 5)
                    collision.objectJump(myObjectName, myObjectControlName, objectName, "Z", -1, i, i + 10)
                    avoidedObjects[objectName] = 1
                elif avoidedObjects[objectName] == 0 and not collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                      objectName, "Z", -1) and \
                        collision.boxesCollisionNoRotations(myObjectName, myObjectControlName, objectName, 0,
                                                            collision.constraints[0][1], -1):
                    collision.objectDodge(myObjectName, myObjectControlName, objectName, "Z", -1, i, i + 15)
                    avoidedObjects[objectName] = 1
            # X from negative to positive
            elif -1 <= orientation <= 1:
                if avoidedObjects[objectName] == 0 and collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                objectName, "X", 1):
                    horse_movements.horseJump(1, i - 5)
                    collision.objectJump(myObjectName, myObjectControlName, objectName, "X", 1, i, i + 10)
                    avoidedObjects[objectName] = 1
                elif avoidedObjects[objectName] == 0 and not collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                      objectName, "X", 1) and \
                        collision.boxesCollisionNoRotations(myObjectName, myObjectControlName, objectName,
                                                            collision.constraints[0][1], 0, 1):
                    collision.objectDodge(myObjectName, myObjectControlName, objectName, "X", 1, i, i + 15)
                    avoidedObjects[objectName] = 1
            # X from positive to negative
            elif 179 <= orientation <= 181 or -181 <= orientation <= -179:
                if avoidedObjects[objectName] == 0 and collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                objectName, "X", -1):
                    horse_movements.horseJump(1, i - 5)
                    collision.objectJump(myObjectName, myObjectControlName, objectName, "X", -1, i, i + 10)
                    avoidedObjects[objectName] = 1
                elif avoidedObjects[objectName] == 0 and not collision.checkIfCanJump(myObjectName, myObjectControlName,
                                                                                      objectName, "X", -1) and \
                        collision.boxesCollisionNoRotations(myObjectName, myObjectControlName, objectName,
                                                            collision.constraints[0][1], 0, 1):
                    collision.objectDodge(myObjectName, myObjectControlName, objectName, "X", -1, i, i + 15)
                    avoidedObjects[objectName] = 1


G = generateRandomDAG("myGraph.txt", (3, 7), (10, 20), (1, 2))
order, longestPath, maxWeight = G.Manhattan()
planeDimension, curves = drawGraphInMaya(G)
placeObstaclesOnMap(curves)
graphTraversalAnimation("C:\Users\Bidi\eclipse-workspace\Animations\horse_movement.mb", "horse", "nurbsCircle5", curves,
                        longestPath)
serializeResults("C:\Users\Bidi\eclipse-workspace\Manhattan\manhattan_results.json", planeDimension, longestPath,
                 curves)

completeAnimation("horse", "nurbsCircle5", 300)