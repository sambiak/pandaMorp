from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, LPoint3, LVector3, BitMask32
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay

BLACK = (0, 0, 0, 1)
WHITE = (1,1,1,0)
MARRON = (0.5,0.25,0,1)
HIGHLIGHT = (0, 1, 1, 1)

def circPos(i,z):
    return LPoint3(3*(i%3) - 3, 3*(i//3) -3,z)
class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()  
        camera.setPosHpr(0, -12, 8, 0, -35, 0)
        """
        self.environ = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
        self.torus = loader.loadModel("torus.egg")
        self.torus.reparentTo(self.render)
        self.torus.setPos(circPos(0,1))
        self.torus.setColor(BLACK)
        self.torus.setScale(0.5,0.5,0.5)
        """
        self.setupLights()
        self.ended = False
        self.currentB = False
        self.firstTurn = True
        # Since we are using collision detection to do picking, we set it up like
        # any other collision detection system with a traverser and a handler
        self.picker = CollisionTraverser()  # Make a traverser
        self.pq = CollisionHandlerQueue()  # Make a handler
        # Make a collision node for our picker ray
        self.pickerNode = CollisionNode('mouseRay')
        # Attach that node to the camera since the ray will need to be positioned
        # relative to it
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        # Everything to be picked will use bit 1. This way if we were doing other
        # collision we could seperate it
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()  # Make our ray
        # Add it to the collision node
        self.pickerNode.addSolid(self.pickerRay)
        # Register the ray as something that can cause collisions
        self.picker.addCollider(self.pickerNP, self.pq)
        self.picker.showCollisions(render)
        self.whiteTurn = True
        # Now we create the chess board and its pieces

        # We will attach all of the squares to their own root. This way we can do the
        # collision pass just on the sqaures and save the time of checking the rest
        # of the scene
        self.batonsRoot = render.attachNewNode("batonsRoot")
        self.batons = [None for i in range(9)]
        self.torus = [[None for j in range(3)] for i in range(9)]
        self.org = [[[None for j in range(3)] for i in range(3)] for i in range(3)]
        for i in range(9):
            # Load, parent, color, and position the model (a single square
            # polygon)
            self.batons[i] = loader.loadModel("bois.egg")
            self.batons[i].reparentTo(self.batonsRoot)
            self.batons[i].setPos(circPos(i,0))
            self.batons[i].setColor(0.75,0.5,0)
            self.batons[i].setScale(0.75,0.75,0.5)
            # Set the model itself to be collideable with the ray. If this model was
            # any more complex than a single polygon, you should set up a collision
            # sphere around it instead. But for single polygons this works
            # fine.
            self.batons[i].find("**/Cylinder").node().setIntoCollideMask(
                BitMask32.bit(1))
            # Set a tag on the square's node so we can look up what square this is
            # later during the collision pass
            self.batons[i].find("**/Cylinder").setTag('baton', str(i))

            # We will use this variable as a pointer to whatever piece is currently
            # in this square
        self.mouseTask = taskMgr.add(self.mouseTask, 'mouseTask')
        self.accept("mouse1", self.click)
        self.accept("w", self.bestPossibleMove)
    def setupLights(self):  # This function sets up some default lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))
    def mouseTask(self, task):
        # This task deals with the highlighting and dragging based on the mouse

        # Check to see if we can access the mouse. We need it to do anything
        # else
        if self.mouseWatcherNode.hasMouse():
            # get the mouse position
            mpos = self.mouseWatcherNode.getMouse()

            # Set the position of the ray based on the mouse position
            self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())

            if self.currentB is not False:
                self.batons[self.currentB].setColor(0.75,0.5,0)
                self.currentB = False

            # Do the actual collision pass (Do it only on the squares for
            # efficiency purposes)
            self.picker.traverse(self.batonsRoot)
            if self.pq.getNumEntries() > 0:
                # if we have hit something, sort the hits so that the closest
                # is first, and highlight that node
                self.pq.sortEntries()
                self.currentB = int(self.pq.getEntry(0).getIntoNode().getTag('baton'))
                # Set the highlight on the picked square
                self.batons[self.currentB].setColor(HIGHLIGHT)
                self.currentB

        return Task.cont
    def click(self):
        if self.currentB is not False and not self.ended:
            self.addTorus(self.currentB)
    def testMorp(self, z, y, x):
        print(z,y,x)
        print([j for j in [self.org[w][y][w]for w in range(3)]if j == None])
        print([j for j in [self.org[w][y][w]for w in range(3)]if j == False])
        print(len([j for j in [self.org[w][y][w]for w in range(3)]if j == False]))
        if len([j for j in self.org[z][y] if j == None]) == 0:
            if len([j for j in self.org[z][y] if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in self.org[z][y] if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j  for j in [self.org[z][w][x]for w in range(3)] if j == None]) == 0:
            if len([j  for j in [self.org[z][w][x]for w in range(3)] if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j  for j in [self.org[z][w][x]for w in range(3)] if j == True]) == 0:
                self.ended = True
                return "blackWin"
                
        if len([j  for j in [self.org[w][y][x]for w in range(3)] if j==None]) == 0:
            if len([j  for j in [self.org[w][y][x]for w in range(3)] if j==False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j  for j in [self.org[w][y][x]for w in range(3)] if j==True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[z][w][w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[z][w][w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[z][w][w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[z][w][2 - w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[z][w][2 - w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[z][w][2 - w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[w][w][x]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[w][w][x]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[w][w][x]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[w][2-w][x]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[w][2-w][x]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[w][2-w][x]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[w][y][w]for w in range(3)]if j == None]) == 0:
            print("wyw")
            if len([j for j in [self.org[w][y][w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[w][y][w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[2-w][y][w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[2-w][y][w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[2-w][y][w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[w][w][w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[w][w][w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[w][w][w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[2-w][w][w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[2-w][w][w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[2-w][w][w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[w][w][2-w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[w][w][2-w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[w][w][2-w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        if len([j for j in [self.org[2-w][w][2-w]for w in range(3)]if j == None]) == 0:
            if len([j for j in [self.org[2-w][w][2-w]for w in range(3)]if j == False]) == 0:
                self.ended = True
                return "whiteWin"
            elif len([j for j in [self.org[2-w][w][2-w]for w in range(3)]if j == True]) == 0:
                self.ended = True
                return "blackWin"
        
            
        return "launched"
    def addTorus(self, i):
        minim = False
        for j,x in enumerate(self.torus[i]):
            if x is None:
                minim = j
                break
        if minim is not False:
            print(minim)
            print(self.whiteTurn)
            print()
            if (self.whiteTurn and not self.firstTurn) or  (self.firstTurn and not (minim == 0 and i//3 == 1 and i%3 == 1)):
                self.torus[i][minim] = loader.loadModel("torus.egg")
                self.torus[i][minim].reparentTo(self.render)
                self.torus[i][minim].setPos(circPos(i,j-1))
                self.torus[i][minim].setColor(WHITE)
                self.torus[i][minim].setScale(0.75,0.75,1.5)
                self.org[minim][i//3][i%3] = self.whiteTurn
                self.whiteTurn = not self.whiteTurn
                if self.firstTurn:
                    self.firstTurn = False
            elif not self.firstTurn:
                self.torus[i][minim] = loader.loadModel("torus.egg")
                self.torus[i][minim].reparentTo(self.render)
                self.torus[i][minim].setPos(circPos(i,j-1))
                self.torus[i][minim].setColor(BLACK)
                self.torus[i][minim].setScale(0.75,0.75,1.5)
                self.org[minim][i//3][i%3] = self.whiteTurn
                self.whiteTurn = not self.whiteTurn
            
            print(self.testMorp(minim, i//3, i%3))
    def possibleMoves(self, state, first):
        possibilities = []
        for r in range(9):
            if (((r is not 4) and first) or (not first)) and state[2][r//3][r%3] == None:
                possibilities.append(r)
        return possibilities
    def bestPossibleMove(self):
        temp = state
        for p in possibleMoves(self, state, first):
            p = 0
    def valeurBranche(self, state, first, Wturn, n):
        vblancs = 0
        vnoirs = 0
        pos = [None for p in possibleMoves(self, state, first) ]
        depth = pos
        for i,p in enumerate(possibleMoves(self, state, first)):
            tempEtat = addTorustemp(p, WTurn, state)
            temp = testMorptemp(tempEtat)
            if temp == 1 and Wturn:
                pos[i] = 1
                depth[i] = n + 1
            elif temp ==0 and Wturn:
                if first:
                    temp2 = valeurBranche(self, temp,not first, not Wturn,n+1)
                    if not (temp2[0] == 0):
                        pos[i] = -temp2[0]
                        depth[i] = temp2[1]
                    else:
                        pos[i] = 0
                        depth[i] = temp2[1]
                else:
                    temp2 = valeurBranche(self, temp, first, not Wturn,n+1)
                    if not (temp2[0] == 0):
                        pos[i] = -temp2[0]
                        depth[i] = temp2[1]
                    else :
                        pos[i] = 0
                        depth[i] = temp2[1]
            elif temp == 2 and (not Wturn):
                pos[i] = 1
            elif temp ==0 and (not Wturn):
                if first:
                    temp2 = valeurBranche(self, temp,not first, not Wturn,n+1)
                    if not (temp2[0] == 0):
                        pos[i] = -temp2[0]
                        depth[i] = temp2[1]
                    else:
                        pos[i] = 0
                        depth[i] = temp2[1]
                else:
                    temp2 = valeurBranche(self, temp, first, not Wturn,n+1)
                    if not (temp2[0] == 0):
                        pos[i] = -temp2[0]
                        depth[i] = temp2[1]
                    else :
                        pos[i] = 0
                        depth[i] = temp2[1]
            else:
                print("tu sais pas coder guillaume")
        if pos == []:
            return (0, n)
        else:
            vic = []
            zero = []
            for i,j in enumerate(pos):
                if j == 1:
                    vic.append(i)
                elif j == 0:
                    zero.append(i)
            if vic is not []:
                return 1, n
            elif zero is not []:
                dmax = 0
                for i in zero:
                    if depth[i] > dmax:
                        dmax = depth[i]
                return 0, dmax
            else:
                return -1, n
                
            
            
                
    def addTorustemp(self, i, whiteTurn, state):
        minim = False
        temp = state
        for j,x in enumerate([state[w][i//3][i%3] for w in range(3)]):
            if x is None:
                minim = j
                break
        if minim is not False:
            print(minim)
            print(whiteTurn)
            temp[minim][i//3][i%3] = whiteTurn
            return temp
    def testMorptemp(self, torg):
        for m in range(27):
            z = m//9
            y = m//3
            x = m%3
            if len([j for j in torg[z][y] if j == None]) == 0:
                if len([j for j in torg[z][y] if j == False]) == 0:
                    return 1
                elif len([j for j in torg[z][y] if j == True]) == 0:
                    return 2
            if len([j  for j in [torg[z][w][x]for w in range(3)] if j == None]) == 0:
                if len([j  for j in [torg[z][w][x]for w in range(3)] if j == False]) == 0:
                    return 1
                elif len([j  for j in [torg[z][w][x]for w in range(3)] if j == True]) == 0:
                    return 2
            if len([j  for j in [torg[w][y][x]for w in range(3)] if j==None]) == 0:
                if len([j  for j in [torg[w][y][x]for w in range(3)] if j==False]) == 0:
                    return 1
                elif len([j  for j in [torg[w][y][x]for w in range(3)] if j==True]) == 0:
                    return 2
            if len([j for j in [torg[z][w][w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[z][w][w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[z][w][w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[z][w][2 - w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[z][w][2 - w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[z][w][2 - w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[w][w][x]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[w][w][x]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[w][w][x]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[w][2-w][x]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[w][2-w][x]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[w][2-w][x]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[w][y][w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[w][y][w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[w][y][w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[2-w][y][w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[2-w][y][w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[2-w][y][w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[w][w][w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[w][w][w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[w][w][w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[2-w][w][w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[2-w][w][w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[2-w][w][w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[w][w][2-w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[w][w][2-w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[w][w][2-w]for w in range(3)]if j == True]) == 0:
                    return 2
            if len([j for j in [torg[2-w][w][2-w]for w in range(3)]if j == None]) == 0:
                if len([j for j in [torg[2-w][w][2-w]for w in range(3)]if j == False]) == 0:
                    return 1
                elif len([j for j in [torg[2-w][w][2-w]for w in range(3)]if j == True]) == 0:
                    return 2
        
            return 0
        

app = MyApp()
app.run()
