import pyxel
import numpy as np

class Music():
    def __init__(self):
        pyxel.sound(0).set(
            notes='c4c4b3b3c4c4a3a3 rrc4c4rrb3b3 rrc4c4b3b3a3a3 c4c4b3c4d4d4e4e4 c4c4b3b3c4c4a3a3 rrc4c4rrb3b3 rrc4c4b3b3a3a3 e4e4d4d4c4d4c4b3 c4c4b3b3c4c4a3a3 rrc4c4rrb3b3 rrc4c4b3b3a3a3 c4c4b3c4d4d4e4e4 c4c4b3b3c4c4a3a3 rrc4c4rrb3b3 rrc4c4b3b3a3a3 g3a3b3c4d4e4f4g4',
            tones='S',
            volumes='4',
            effects='NF',
            speed=10)

        pyxel.sound(1).set(
            notes='e3e3e3e3 c3d3e3d3 r g3g3g3 f3f3e3e3 d3d3d3d3 b2c3d3c3 r e3e3e3 d3d3c3c3 a2a2b2b2 c3c3a2a2 b2b2c3c3 d3d3e3e3 f3f3e3e3 d#3d#3e3e3 a3a3g3g3 e3f3e3d3',
            tones='T',
            volumes='4',
            effects='V',
            speed=20)

        pyxel.sound(2).set(
            notes='e3e3e3e3 c3d3e3d3 r g3g3g3 f3f3e3e3 d3d3d3d3 b2c3d3c3 r e3e3e3 d3d3c3c3 a2a2b2b2 c3c3a2a2 b2b2c3c3 d3d3e3e3 f3f3e3e3 f3f3g3g3 a3a3g#3g#3 a3a3b3b3',
            tones='T',
            volumes='4',
            effects='V',
            speed=20)

        pyxel.sound(3).set(
            notes='rrd3r rc3rr rrd3r rc3rr rrf3r re3rr rrg3r rf#3rr',
            tones='S',
            volumes='3',
            effects='F',
            speed=20)

        pyxel.sound(4).set(
            notes='rrd3r rc3rr rrd3r rc3rr rrg3r rf#3rr rrg#3r rg#3',
            tones='S',
            volumes='3',
            effects='F',
            speed=20)

        pyxel.sound(5).set(
            notes='e4f4e4d4',
            tones='S',
            volumes='3',
            effects='N',
            speed=10)

        pyxel.sound(16).set(
            notes='rrrrrrrrrrrrrrrr',
            tones='T',
            volumes='4',
            effects='F',
            speed=80)

        pyxel.sound(17).set(
            notes='e3d3e3c3 re3rd3 re3d3c3 e3e3f3g3 e3d3e3c3 re3rd3 re3d3c3 g3f3e3d3 e3d3e3c3 re3rd3 re3d3c3 e3e3f3g3 e3d3e3c3 re3rd3 re3d3c3 g3f3e3d3',
            tones='T',
            volumes='4',
            effects='F',
            speed=20)

        pyxel.sound(18).set(
            notes='a2c3a2c3 a2c3a2c3 a2c3a2c3 a2c3a2c3 g2b2g2b2 g2b2g2b2 c3e3c3e3 c3e3c3e3 f2a2f2a2 f2a2f2a2 b2f3b2f3 b2f3b2d3 e3g3e3g3 e3g3e3g3 b-2e3b-2e3 b-2g3b-2g3',
            tones='T',
            volumes='2',
            effects='F',
            speed=20)

        pyxel.sound(19).set(
            notes='a2c3a2c3 a2c3a2c3 a2c3a2c3 a2c3a2c3 g2b2g2b2 g2b2g2b2 c3e3c3e3 c3e3c3e3 f2a2f2a2 f2a2f2a2 a2c3a2c3 a2c3a2c3 b2d3b2d3 b2d3b2d3 g#2d3g#2d3 g#2d3g#2d3',
            tones='T',
            volumes='2',
            effects='F',
            speed=20)

        pyxel.sound(20).set(
            notes='rrg3r rg3rr rrg3r rg3rr rrg3r rg3rr rra3r ra3rr',
            tones='S',
            volumes='3',
            effects='F',
            speed=20)

        pyxel.sound(21).set(
            notes='rrg3r rg3rr rrg3r rg3rr rra3r ra3rr rrc4r rb3rr',
            tones='S',
            volumes='3',
            effects='F',
            speed=20)

        pyxel.sound(32).set(
            notes='a1a2e2a2 a1a2e2a1 a1a2e2a2 a1a2e2a1 g1g2d2g2 g1g2d2g1 g1g2d2g2 g1g2d2g1 f#1f#2d2f#2 f#1f#2d2f#1 f#1f#2d2f#2 f#1f#2d2f#1 f1f2c2f2 f1f2c2f1 g1g2d2g1 g1g2d2g1',
            tones='P',
            volumes='4',
            effects='F',
            speed=20)

        pyxel.sound(33).set(
            notes='a0a1e1a1 a0a1e1a0 a0a1e1a1 a0a1e1a0 g0g1d1g1 g0g1d1g0 g0g1d1g1 g0g1d1g0 f#0f#1d1f#1 f#0f#1d1f#0 f#0f#1d1f#1 f#0f#1d1f#0 f0f1c1f1 f0f1c1f0 g0g1d1g0 g0g1d1g1',
            tones='P',
            volumes='4',
            effects='F',
            speed=20)

        pyxel.sound(34).set(
            notes='f1f1f2f1 f1f1f2f1 f1f1f2f1 f1f1f2f1 e1e1e2e1 e1e1e2e1 a1a1a2a1 a1a1a2a1 d1d1d2d1 d1d1d2d1 g1g1g2g1 g1g1g2g1 c2c2g2c2 c2c2g2c2 c1c1c2c1 c1c1c2c1',
            tones='P',
            volumes='3',
            effects='NNFN NFFF',
            speed=20)

        pyxel.sound(35).set(
            notes='f1f1f2f1 f1f1f2f1 f1f1f2f1 f1f1f2f1 e1e1e2e1 e1e1e2e1 a1a1a2a1 a1a1a2a1 d1d1d2d1 d1d1d2d1 f1f1f2f1 f1f1f2f1 g1g1g2g1 g1g1g2g1 e1e1e2e1 e1e1e2e1',
            tones='P',
            volumes='4',
            effects='NNFN NFFF',
            speed=20)

        pyxel.sound(36).set(
            notes='a0a0a0a0 g1a1a1d1 e1e1c1d1 d1b0c1c1 g0g0g0g0 g1a1a1d1 e1e1c1d1 d1b0c1c1 f#0f#0f#0f#0 g1a1a1d1 e1e1c1d1 d1b0c1c1 f0f0f0f0 g1a1a1d1 e1e1c1d1 d1b0c1c1',
            tones='P',
            volumes='5',
            effects='NFNF NNFN NFNN FNNF',
            speed=10)

        pyxel.sound(37).set(
            notes='a0a0a2r ra2rr a0a0a2r ra2rr c1c1c3r rc3rr d1d1d3r rd3d2d1',
            tones='P',
            volumes='4',
            effects='F',
            speed=20)

        pyxel.sound(38).set(
            notes='a0e1a1a0 e1a1a0e1 a1a0e1a1 a0e1a1a0 d1a1d2d1 a1d2d1a1 e1b1e2e1 b1e2b2e3',
            tones='P',
            volumes='4',
            effects='F',
            speed=20)

        pyxel.music(0).set([0,0,1, 2, 0, 3, 4, 5],[16,17,18, 19, 17, 20, 21],[32, 33, 34, 35, 36, 36, 37, 38],[])

        pyxel.sound(40).set(
            notes='c3c3c3c3 c3c3c3c3 c3c3c3c3 c3c3c3c3',
            tones='N',
            volumes='6',
            effects='F',
            speed=5)

        pyxel.sound(41).set(
            notes='b4g4e4d4 c4b3a3g3 f3e3d3c3 b2a2g2f2 e2d2c2 r c1c1c1 c1c1c1 c1c1c1 c1c1 c1 r c1',
            tones='N',
            volumes='7',
            effects='ssss ssss ssss ssss ssss n nnf nnf nnf nf f n f',
            speed=5)

        pyxel.sound(42).set(
            notes='c1c1c1 c1c1c1 c1c1c1 c1c1c1 c1c1 c1 r c1',
            tones='N',
            volumes='4',
            effects='nnf nnf nnf nnf nf f n f',
            speed=5)

        pyxel.sound(43).set(
            notes='f3e3d3c3 b2a2g2f2 e2d2c2',
            tones='N',
            volumes='4',
            effects='nnnn nnnn nnn',
            speed=5)

        pyxel.music(1).set([42], [43], [], [])

        pyxel.sound(44).set(
            notes='rr f3f3f3 f3f3f3 g3g3g3 g3g3g3 a3a3a3 a3a3a3',
            tones='T',
            volumes='5',
            effects='nn nff fff nff fff nnn nnf',
            speed=25)

        pyxel.sound(45).set(
            notes='rr a3a3a3 a3a3a3 b3b3b3 b3b3b3 c#4c#4c#4 c#4c#4c#4 c#4c#4',
            tones='T',
            volumes='5',
            effects='nn nff fff nff fff nnv vvf nf',
            speed=25)

        pyxel.sound(46).set(
            notes='rr c4c4c4 c4c4c4 d4d4d4 d4d4d4 e4e4e4 e4e4e4 a4a4',
            tones='T',
            volumes='5',
            effects='nn nff fff nff fff nnv vvf nf',
            speed=25)

        pyxel.music(2).set([44], [45], [46], [])

class Start():
    def __init__(self):
        pyxel.init(200,200, fps = 18)
        Music()
        self.counter = 0
        self.flag = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.flag = True
        if self.flag == True:
            self.counter += 1
        if self.counter == 18:
            App(1)

    def draw(self):
        pyxel.cls(0)
        if self.flag == True:
            pyxel.text(75, 95, "S T A G E  1", 7)
            pyxel.text(80, 110, "5 Targets", 7)
        else:
            pyxel.text(67, 75, "FLIGHT - SHOOTING", 7)
            pyxel.line(60, 82, 140, 82, 5)
            pyxel.text(67, 95, "KEY_SPACE : START", pyxel.frame_count % 16)
            pyxel.rectb(30, 123, 140, 40, 1)
            pyxel.text(80, 130, "USER GUIDE", 13)
            pyxel.text(40, 140, " FLIGHT  : KEY_LEFT & KEY_RIGHT", 7)
            pyxel.text(40, 150, "SHOOTING : KEY_SPACE", 7)

class Game_Over():
    def __init__(self, stage_num):
        pyxel.stop()
        pyxel.playm(1)
        self.stage_num = stage_num
        self.flag = False
        self.counter = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.flag = True
        if self.flag == True:
            self.counter += 1
        if self.counter == 18:
            pyxel.playm(0, loop = True)
            App(self.stage_num)

    def draw(self):
        pyxel.cls(0)
        if self.flag == False:
            pyxel.text(68, 70, "G A M E  O V E R", 7)
            pyxel.line(60, 78, 140, 78, 5)
        if self.flag == True:
            pyxel.text(75, 95, "S T A G E  " + str(self.stage_num), 7)
        elif pyxel.frame_count % 20 < 14:
            pyxel.text(53, 95, "KEY_SPACE : RETRY STAGE " + str(self.stage_num), 7)

class Next_Stage():
    def __init__(self, stage_num):
        self.stage_num = stage_num + 1
        self.flag = False
        self.counter = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.flag = True
        if self.flag == True:
            self.counter += 1
        if self.counter == 18:
            App(self.stage_num)

    def draw(self):
        pyxel.cls(0)
        if self.flag == False:
            pyxel.text(75, 70, "STAGE CLEAR !", pyxel.frame_count % 16)
            pyxel.line(60, 78, 140, 78, 5)
        if self.flag == True:
            pyxel.text(75, 95, "S T A G E  " + str(self.stage_num), 7)
            if self.stage_num == 3:
                pyxel.text(82, 70, "F I N A L", pyxel.frame_count % 16)
                pyxel.text(80, 110, "20 Targets", 7)
            else:
                pyxel.text(80, 110, "10 Targets", 7)
        elif pyxel.frame_count % 20 < 14:
            pyxel.text(55, 95, "KEY_SPACE : NEXT STAGE " + str(self.stage_num), 7)

class Game_Clear():
    def __init__(self):
        pyxel.stop()
        pyxel.playm(2)
        self.flag = False
        self.counter = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.flag = True
        if self.flag == True:
            self.counter += 1
        if self.counter == 18:
            App(1)

    def draw(self):
        pyxel.cls(0)
        if self.flag == False:
            pyxel.text(75, 70, "GAME CLEAR !!", pyxel.frame_count % 16)
            pyxel.line(60, 78, 140, 78, 5)
        if self.flag == True:
            pyxel.text(75, 95, "S T A G E  1", 7)
        elif pyxel.frame_count % 20 < 14:
            pyxel.text(65, 95, "KEY_SPACE : RESTART", 7)

class Fighter():
    def __init__(self):
        self.tx = -60
        self.ty = 0
        self.dir = 0
        self.bank = 0
        self.vertexs = np.array([[100,-100,-100,100],[100,100,-100,-100],[1, 1, 1, 1]]) # ワールド
        self.k = 1800   # 線分の上下幅を決める定数

        self.charge = 8     # 3: 緑, 8: 赤, 10: 黄
        self.horizontal = 3 # 3: 緑, 8: 赤, 10: 黄


    def move(self, App):
        self.list1 = []
        if self.horizontal != 10:    # rocked だと操作できない
            if pyxel.btn(pyxel.KEY_LEFT):
                if self.bank < 34:
                    self.bank += 1.7
                    self.horizontal = 8  # 赤
            if pyxel.btn(pyxel.KEY_RIGHT):
                if self.bank > -34:
                    self.bank -= 1.7
                    self.horizontal = 8  # 赤
            if pyxel.btn(pyxel.KEY_LEFT) == False:
                if self.bank > 1:
                    self.bank -= 0.7
                elif self.bank > 0:
                    self.bank = 0
                    self.horizontal = 3  # 緑
            if pyxel.btn(pyxel.KEY_RIGHT) == False:
                if self.bank < -1:
                    self.bank += 0.7
                elif self.bank < 0:
                    self.bank = 0
                    self.horizontal = 3  # 緑

        self.dir += self.bank / 20                # 旋回性能の定数
        speed = (140 - abs(self.bank))/300   # スピードの定数

        self.m1 = pyxel.sin(self.dir); self.m2 = pyxel.cos(self.dir)

        self.tx += self.m2 * speed
        self.ty += self.m1 * speed

        if self.tx > 65 or self.tx < -65 or self.ty > 65 or self.ty < -65:
            App.warning = True

        self.f_trns = np.array([
            [self.m2, self.m1, -self.tx * self.m2 - self.ty * self.m1],
            [-self.m1, self.m2, self.tx * self.m1 - self.ty * self.m2],
            [0, 0, 1]])

        self.f_vert = np.dot(self.f_trns, self.vertexs)
        self.f_cos = [self.f_vert[0, 0] / np.sqrt(self.f_vert[0, 0]**2 + self.f_vert[1, 0]**2),
            self.f_vert[0, 1] / np.sqrt(self.f_vert[0, 1]**2 + self.f_vert[1, 1]**2),
            self.f_vert[0, 2] / np.sqrt(self.f_vert[0, 2]**2 + self.f_vert[1, 2]**2),
            self.f_vert[0, 3] / np.sqrt(self.f_vert[0, 3]**2 + self.f_vert[1, 3]**2)]

        for i in range (4):
            if 0.554 < self.f_cos[i]:
                self.list1.append(i)

        if len(self.list1) == 0:
            self.scr = np.ones((3, 4)) # 行列を作成, データ数は4
            s = int(((self.dir + 45) % 360) // 90)
            aa = self.f_vert[0, s]; bb = self.f_vert[1, s]
            cc = self.f_vert[0, s-1]; dd = self.f_vert[1, s-1]
            if aa == cc:
                self.scr[0, 0] = -120; self.scr[1, 0] = self.k / aa    # 左端
                self.scr[0, 1] = -120; self.scr[1, 1] = -self.k / aa
                self.scr[0, 2] = 120; self.scr[1, 2] = self.k / aa     # 右端
                self.scr[0, 3] = 120; self.scr[1, 3] = -self.k / aa

            else:
                tk = (bb - dd) / (aa - cc)
                tt1 = (tk - 1.5) / (tk * aa - bb)
                tt2 = (tk + 1.5) / (tk * aa - bb)
                self.scr[0, 0] = -120; self.scr[1, 0] = self.k * tt1   # 左端
                self.scr[0, 1] = -120; self.scr[1, 1] = -self.k * tt1
                self.scr[0, 2] = 120; self.scr[1, 2] = self.k * tt2    # 右端
                self.scr[0, 3] = 120; self.scr[1, 3] = -self.k * tt2



        elif len(self.list1) == 1:
            self.scr = np.ones((3, 6)) # 行列を作成, データ数は6
            s = self.list1[0]
            aa = self.f_vert[0, s]; bb = self.f_vert[1, s]
            cc = self.f_vert[0, s-1]; dd = self.f_vert[1, s-1]
            ee = self.f_vert[0, s-3]; ff = self.f_vert[1, s-3]
            if aa == cc:
                self.scr[0, 0] = -80 * bb / aa; self.scr[1, 0] = self.k / aa   # 頂点
                self.scr[0, 1] = -80 * bb / aa; self.scr[1, 1] = -self.k / aa
                self.scr[0, 2] = -120; self.scr[1, 2] = 1.5 * self.k / bb      # 左端
                self.scr[0, 3] = -120; self.scr[1, 3] = -1.5 * self.k / bb
                self.scr[0, 4] = 120; self.scr[1, 4] = self.k / aa             # 右端
                self.scr[0, 5] = 120; self.scr[1, 5] = -self.k / aa

            elif aa == ee:
                self.scr[0, 0] = -80 * bb / aa; self.scr[1, 0] = self.k / aa   # 頂点
                self.scr[0, 1] = -80 * bb / aa; self.scr[1, 1] = -self.k / aa
                self.scr[0, 2] = -120; self.scr[1, 2] = self.k / aa            # 左端
                self.scr[0, 3] = -120; self.scr[1, 3] = -self.k / aa
                self.scr[0, 4] = 120; self.scr[1, 4] = -1.5 * self.k / bb      # 右端
                self.scr[0, 5] = 120; self.scr[1, 5] = 1.5 * self.k / bb

            else:
                tk1 = (bb - ff) / (aa - ee)
                tt1 = (tk1 - 1.5) / (tk1 * aa - bb)
                tk2 = (bb - dd) / (aa - cc)
                tt2 = (tk2 + 1.5) / (tk2 * aa - bb)
                self.scr[0, 0] = -80 * bb / aa; self.scr[1, 0] = self.k / aa   # 頂点
                self.scr[0, 1] = -80 * bb / aa; self.scr[1, 1] = -self.k / aa
                self.scr[0, 2] = -120; self.scr[1, 2] = self.k * tt1           # 左端
                self.scr[0, 3] = -120; self.scr[1, 3] = -self.k * tt1
                self.scr[0, 4] = 120; self.scr[1, 4] = self.k * tt2            # 右端
                self.scr[0, 5] = 120; self.scr[1, 5] = -self.k * tt2

        elif len(self.list1) == 2:
            self.scr = np.ones((3, 8)) # 行列を作成, データ数は8
            if self.list1 == [0, 3]:
                s = 3
            else:
                s = self.list1[0]
            aa = self.f_vert[0, s]; bb = self.f_vert[1, s]
            cc = self.f_vert[0, s-3]; dd = self.f_vert[1, s-3]
            ee = self.f_vert[0, s-2]; ff = self.f_vert[1, s-2]
            gg = self.f_vert[0, s-1]; hh = self.f_vert[1, s-1]
            tk1 = (dd - ff) / (cc - ee)
            tt1 = (tk1 - 1.5) / (tk1 * cc - dd)
            tk2 = (bb - hh) / (aa - gg)
            tt2 = (tk2 + 1.5) / (tk2 * aa - bb)
            self.scr[0, 0] = -80 * dd / cc; self.scr[1, 0] = self.k / cc   # 頂点(左)
            self.scr[0, 1] = -80 * dd / cc; self.scr[1, 1] = -self.k / cc
            self.scr[0, 2] = -80 * bb / aa; self.scr[1, 2] = self.k / aa   # 頂点(右)
            self.scr[0, 3] = -80 * bb / aa; self.scr[1, 3] = -self.k / aa
            self.scr[0, 4] = -120; self.scr[1, 4] = self.k * tt1           # 左端
            self.scr[0, 5] = -120; self.scr[1, 5] = -self.k * tt1
            self.scr[0, 6] = 120; self.scr[1, 6] = self.k * tt2            # 右端
            self.scr[0, 7] = 120; self.scr[1, 7] = -self.k * tt2

        else:
            self.scr = np.ones((3, 10)) # 行列を作成, データ数は10
            s = 6 - self.list1[0] - self.list1[1] - self.list1[2]  # s = 0, 1, 2, 3
            aa = self.f_vert[0, s-3]; bb = self.f_vert[1, s-3]
            cc = self.f_vert[0, s-2]; dd = self.f_vert[1, s-2]
            ee = self.f_vert[0, s-1]; ff = self.f_vert[1, s-1]
            gg = self.f_vert[0, s]; hh = self.f_vert[1, s]        # 見えない頂点
            tk1 = (ff - hh) / (ee - gg)
            tt1 = (tk1 - 1.5) / (tk1 * ee - ff)
            tk2 = (bb - hh) / (aa - gg)
            tt2 = (tk2 + 1.5) / (tk2 * aa - bb)
            self.scr[0, 0] = -80 * ff / ee; self.scr[1, 0] = self.k / ee   # 頂点(左)
            self.scr[0, 1] = -80 * ff / ee; self.scr[1, 1] = -self.k / ee
            self.scr[0, 2] = -80 * dd / cc; self.scr[1, 2] = self.k / cc   # 頂点(中)
            self.scr[0, 3] = -80 * dd / cc; self.scr[1, 3] = -self.k / cc
            self.scr[0, 4] = -80 * bb / aa; self.scr[1, 4] = self.k / aa   # 頂点(右)
            self.scr[0, 5] = -80 * bb / aa; self.scr[1, 5] = -self.k / aa
            self.scr[0, 6] = -120; self.scr[1, 6] = self.k * tt1           # 左端
            self.scr[0, 7] = -120; self.scr[1, 7] = -self.k * tt1
            self.scr[0, 8] = 120; self.scr[1, 8] = self.k * tt2            # 右端
            self.scr[0, 9] = 120; self.scr[1, 9] = -self.k * tt2

        self.r1 = pyxel.sin(self.bank); self.r2 = pyxel.cos(self.bank)
        self.rotation = np.array([[self.r2, self.r1, 0],[-self.r1, self.r2, 0],[0, 0, 1]])

        src1 = np.dot(self.rotation, self.scr)
        self.scr2 = np.dot(np.array([[1,0,100], [0,-1,100], [0,0,1]]), src1)


    def draw_back(self):
        if len(self.list1) == 0:
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 2], self.scr2[1, 2], 6)
            pyxel.line(self.scr2[0, 1], self.scr2[1, 1], self.scr2[0, 3], self.scr2[1, 3], 6)
        elif len(self.list1) == 1:
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 1], self.scr2[1, 1], 6)
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 2], self.scr2[1, 2], 6)
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 4], self.scr2[1, 4], 6)
            pyxel.line(self.scr2[0, 1], self.scr2[1, 1], self.scr2[0, 3], self.scr2[1, 3], 6)
            pyxel.line(self.scr2[0, 1], self.scr2[1, 1], self.scr2[0, 5], self.scr2[1, 5], 6)
        elif len(self.list1) == 2:
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 1], self.scr2[1, 1], 6)
            pyxel.line(self.scr2[0, 2], self.scr2[1, 2], self.scr2[0, 3], self.scr2[1, 3], 6)
            pyxel.line(self.scr2[0, 4], self.scr2[1, 4], self.scr2[0, 0], self.scr2[1, 0], 6)
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 2], self.scr2[1, 2], 6)
            pyxel.line(self.scr2[0, 2], self.scr2[1, 2], self.scr2[0, 6], self.scr2[1, 6], 6)
            pyxel.line(self.scr2[0, 5], self.scr2[1, 5], self.scr2[0, 1], self.scr2[1, 1], 6)
            pyxel.line(self.scr2[0, 1], self.scr2[1, 1], self.scr2[0, 3], self.scr2[1, 3], 6)
            pyxel.line(self.scr2[0, 3], self.scr2[1, 3], self.scr2[0, 7], self.scr2[1, 7], 6)
        else:
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 1], self.scr2[1, 1], 6)
            pyxel.line(self.scr2[0, 2], self.scr2[1, 2], self.scr2[0, 3], self.scr2[1, 3], 6)
            pyxel.line(self.scr2[0, 4], self.scr2[1, 4], self.scr2[0, 5], self.scr2[1, 5], 6)
            pyxel.line(self.scr2[0, 6], self.scr2[1, 6], self.scr2[0, 0], self.scr2[1, 0], 6)
            pyxel.line(self.scr2[0, 0], self.scr2[1, 0], self.scr2[0, 2], self.scr2[1, 2], 6)
            pyxel.line(self.scr2[0, 2], self.scr2[1, 2], self.scr2[0, 4], self.scr2[1, 4], 6)
            pyxel.line(self.scr2[0, 4], self.scr2[1, 4], self.scr2[0, 8], self.scr2[1, 8], 6)
            pyxel.line(self.scr2[0, 7], self.scr2[1, 7], self.scr2[0, 1], self.scr2[1, 1], 6)
            pyxel.line(self.scr2[0, 1], self.scr2[1, 1], self.scr2[0, 3], self.scr2[1, 3], 6)
            pyxel.line(self.scr2[0, 3], self.scr2[1, 3], self.scr2[0, 5], self.scr2[1, 5], 6)
            pyxel.line(self.scr2[0, 5], self.scr2[1, 5], self.scr2[0, 9], self.scr2[1, 9], 6)


class Bullet():
    color = [8, 14, 7]
    def __init__(self):
        self.flag = False

    def shoot(self, tx, ty, m1, m2, counter_1):
        self.flag = True
        self.x = tx + (4 * m2)
        self.y = ty + (4 * m1)
        self.vx = 8*m2
        self.vy = 8*m1
        self.col = counter_1 % 3
        self.which = 1 if counter_1 % 2 == 0 else -1

    def move(self, f1, targets, App):
        self.x += self.vx
        self.y += self.vy
        if self.x > 95 or self.x < -95 or self.y > 95 or self.y < -95:
            self.flag = False
        else:
            for target in targets:
                if target.explosion == 0 and (self.x - target.position[0,0])**2 + (self.y - target.position[1,0])**2 < 35:
                    self.flag = False
                    target.flag = True  # 爆発
                    App.kill_counter += 1


        if self.flag == True:
            w1 = np.array([[self.x], [self.y], [1]])
            self.w2 = np.dot(f1.f_trns, w1)
            self.f_bull = np.array([[80*self.w2[1, 0] / self.w2[0, 0]], [320 / self.w2[0, 0]] , [1]])

class Target():
    def __init__(self, x, y):
        self.position = np.array([[x],[y],[1]])     # ワールドマップ上で、(x, y, 1)
        self.scr1 = np.array([[0],[0],[1]])
        self.flag = False             # flag:: 弾丸に当たった瞬間に True
        self.explosion = 0            # flag:: non-exist : -1(44), exist : 0, explosion : 1 ~ 43

    def move(self, trns, rotation, App):
        distance = (self.position[0,0] - App.f1.tx) **2 + (self.position[1,0] - App.f1.ty) ** 2
        if distance < 42:
            App.game_over = True
        elif distance < 500:
            App.warning = True
        self.f_position = np.dot(trns, self.position)
        if self.flag == True:
            self.explosion += 1
            if self.explosion == 44:
                self.explosion = -1
                self.flag = False

        if self.f_position[0,0] > 3:
            self.scr1[0,0] = -80 * self.f_position[1,0] / self.f_position[0,0]
            self.scr1[1,0] = 0
            self.radius = 500 / self.f_position[0,0]     # 500 は半径を決める定数
            scr2 = np.dot(rotation, self.scr1)
            self.scr3 = np.dot(np.array([[1,0,100], [0,-1,100], [0,0,1]]), scr2)
        else:
            self.scr3 = np.array([[-10],[-10],[1]])
            self.radius = 0

    def draw(self, col, App):
        if self.explosion == -1:
            pass
        elif self.explosion < 15:
            pyxel.circ(self.scr3[0,0], self.scr3[1,0], self.radius, col)
        elif self.explosion == 15:
            pyxel.play(3, 41)
            if App.stage_num == 1:
                if len(App.targets) < 9:
                    self.build(App)
                    self.build(App)
            elif App.stage_num == 2:
                if len(App.targets) < 16:
                    self.build(App)
                    self.build(App)
                    self.build(App)
            else:
                if len(App.targets) < 40:
                    self.build(App)
                    self.build(App)
                    self.build(App)
                    self.build(App)
        elif self.explosion < 18:
            pass
        elif self.explosion < 20:
            pyxel.circ(self.scr3[0,0], self.scr3[1,0], 0.5 * self.radius, col)
        else:
            if self.explosion % 3 == 0:
                pyxel.circ(self.scr3[0,0], self.scr3[1,0], (self.explosion - 16) * 0.1 * self.radius, 8)
            elif self.explosion % 3 == 1:
                pyxel.circ(self.scr3[0,0], self.scr3[1,0], (self.explosion - 13) * 0.1 * self.radius, 10)

    def build(self, App):
        a = pyxel.rndi(-70, 70); b = pyxel.rndi(-70, 70)
        if (App.f1.tx - a)**2 + (App.f1.ty - b)**2 > 800:
            App.targets.append(Target(a, b))
            App.targets[-1].f_position = np.dot(App.f1.f_trns, App.targets[-1].position)
            if App.targets[-1].f_position[0,0] > 3:
                App.targets[-1].scr1[0,0] = -80 * App.targets[-1].f_position[1,0] / App.targets[-1].f_position[0,0]
                App.targets[-1].scr1[1,0] = 0
                App.targets[-1].radius = 500 / App.targets[-1].f_position[0,0]     # 500 は半径を決める定数
                scr2 = np.dot(App.f1.rotation, App.targets[-1].scr1)
                App.targets[-1].scr3 = np.dot(np.array([[1,0,100], [0,-1,100], [0,0,1]]), scr2)
            else:
                App.targets[-1].scr3 = np.array([[-10],[-10],[1]])
                App.targets[-1].radius = 0
        else:
            self.build(App)


class App():

    def __init__(self, stage_num):
        self.stage_num = stage_num
        self.kill_counter = 0
        self.next = 0
        if self.stage_num == 1:
            pyxel.playm(0, loop = True)
            self.col = 3
        elif self.stage_num == 2:
            self.col = 4
        else:
            self.col = 2
        self.game_over = False
        self.f1 = Fighter()
        self.bullets = [Bullet() for i in range(12)]
        self.warning = False

        self.targets = [Target(60, 0)]

        self.shooting = False        # shooting flag

        self.charge_str = [0, 1, 2, "ready", 4, 5, 6, 7, "charging", 9, "shooting"]
        self.horizontal_str = [0, 1, 2, "horizontal", 4, 5, 6, 7, "inclined", 9, "rocked"]

        self.counter_1 = 0
        self.counter_2 = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        self.warning = False
        if (self.f1.tx < -85) or (self.f1.tx > 85):
            self.game_over = True
        if (self.f1.ty < -85) or (self.f1.ty > 85):
            self.game_over = True

        if self.stage_num == 1 and self.kill_counter >= 5:
            self.next += 1
        elif self.stage_num == 2 and self.kill_counter >= 10:
            self.next += 1
        elif self.stage_num == 3 and self.kill_counter >= 20:
            self.next += 1

        if self.next == 30:
            if self.stage_num == 3:
                Game_Clear()
            else:
                Next_Stage(self.stage_num)

        self.f1.move(self)

        for elem in self.targets:
            if elem.explosion != -1:
                elem.move(self.f1.f_trns, self.f1.rotation, self)


        if pyxel.btnp(pyxel.KEY_SPACE) and self.f1.charge == 3 and self.f1.horizontal == 3:
            pyxel.play(3, 40)
            self.shooting = True        # flag を True に切り替え
            self.f1.charge = 10         # それぞれ黄色に変更
            self.f1.horizontal = 10

        if self.shooting == True and self.counter_1 < 12:
            self.bullets[self.counter_1].shoot(self.f1.tx, self.f1.ty, self.f1.m1, self.f1.m2, self.counter_1)

        for elem in self.bullets:
            if elem.flag == True:
                elem.move(self.f1, self.targets, self)

        if self.shooting == True:
            self.counter_1 += 1

        if self.counter_1 == 32:
            self.counter_1 = 0
            self.f1.charge = 8
            self.f1.horizontal = 3
            self.shooting = False

        if self.f1.charge == 8:
            self.counter_2 += 1

        if self.counter_2 == 90:
            self.counter_2 = 0
            self.f1.charge = 3


    def draw(self):
        if self.game_over == True:
            Game_Over(self.stage_num)
        pyxel.cls(0)

        self.f1.draw_back()

        for elem in self.targets:
            if elem.explosion != -1:
                elem.draw(self.col, self)

        for elem in self.bullets:   # 弾丸
            if elem.flag == True:
                pyxel.pset(100 + elem.f_bull[0, 0] + 120 * elem.which / elem.w2[0, 0], 98 + elem.f_bull[1, 0], Bullet.color[elem.col])

        self.draw_cockpit()



    def draw_cockpit(self):
        if self.warning == True:
            if pyxel.frame_count % 20 < 14:
                pyxel.line(0, 0, 0, 200, 8)
                pyxel.line(199, 0, 199, 200, 8)
                pyxel.text(75, 50, "W A R N I N G", 8)
                pyxel.line(70, 46, 129, 46, 8)
                pyxel.line(70, 58, 129, 58, 8)
        pyxel.tri(0, 0, 0, 35, 35, 0, 1)    # 上部フレーム
        pyxel.tri(164, 0, 199, 0, 199, 35, 1)

        pyxel.rect(0, 164, 200, 36, 1)      # コントロールパネル
        pyxel.rect(50, 140, 100, 24, 1)
        pyxel.tri(0, 164, 49, 140, 49, 164, 1)
        pyxel.tri(150, 140, 150, 164, 199, 164, 1)

        pyxel.rect(75, 147, 50, 50, 0)  # マップの中心は(99, 171)
        pyxel.rectb(77, 149, 46, 46, 6)
        for elem in self.targets:
            if elem.explosion != -1:
                pyxel.circ(99 + elem.position[0,0]/4, 171 - elem.position[1,0]/4, 2, self.col)
        pyxel.circ(99 + self.f1.tx/4, 171 - self.f1.ty/4, 2, 9)


        pyxel.circ(30, 180, 15, 0)     # 姿勢指示器の中心は(30, 180)
        pyxel.line(30+15*self.f1.r2, 180+15*self.f1.r1, 30-15*self.f1.r2, 180-15*self.f1.r1, 8)
        pyxel.tri(30, 165, 27, 170, 33, 170, 8)
        pyxel.pset(30, 180, 10); pyxel.pset(29, 180, 9); pyxel.pset(31, 180, 9); pyxel.pset(30, 181, 9); pyxel.pset(30, 179, 9)
        pyxel.line(18, 179, 26, 179, 9)
        pyxel.line(34, 179, 42, 179, 9)
        pyxel.line(21, 184, 27, 182, 9)
        pyxel.line(33, 182, 39, 184, 9)
        pyxel.line(26, 179, 27, 182, 9)
        pyxel.line(34, 179, 33, 182, 9)

        pyxel.rect(50, 180, 21, 7, 0)   # ターゲットの数
        pyxel.text(52, 181, str(self.kill_counter), 7)
        pyxel.text(59, 181, "/", 7)
        if self.stage_num == 1:
            pyxel.text(63, 181, "5", 7)
        elif self.stage_num == 2:
            pyxel.text(63, 181, "10", 7)
        else:
            pyxel.text(63, 181, "20", 7)

        pyxel.circ(57, 161, 13, 0)     # コンパスの中心は(57, 161)
        pyxel.pset(57, 148, 8); pyxel.pset(57, 174, 8); pyxel.pset(44, 161, 8); pyxel.pset(70, 161, 8)
        pyxel.pset(57, 147, 8); pyxel.pset(57, 173, 8); pyxel.pset(45, 161, 8); pyxel.pset(69, 161, 8)
        pyxel.line(57, 161, 57 + 12 * self.f1.m2, 161 - 12 * self.f1.m1, 9)
        pyxel.circb(57, 161, 7, 13)

        pyxel.rect(141, 160, 30, 7, 0)
        pyxel.text(143, 161, "STAGE " + str(self.stage_num), 13)

        pyxel.rectb(132, 170, 7, 7, 0)
        pyxel.rect(133, 171, 5, 5, self.f1.horizontal)
        pyxel.rect(141, 170, 45, 7, 0)
        pyxel.text(143, 171, self.horizontal_str[self.f1.horizontal], 13)

        pyxel.rectb(132, 180, 7, 7, 0)
        pyxel.rect(133, 181, 5, 5, self.f1.charge)
        pyxel.rect(141, 180, 45, 7, 0)
        pyxel.text(143, 181, self.charge_str[self.f1.charge], 13)

        pyxel.rect(141, 188, 45, 2, 0)      # チャージメーター
        if self.f1.charge == 3:
            pyxel.rect(141, 188, 45, 2, 3)
        else:
            pyxel.rect(141, 188, self.counter_2 / 2, 2, 8)

        pyxel.circb(100, 100, 30, 13)       # 照準
        if self.f1.horizontal == 3 and self.f1.charge == 3:
            pyxel.circb(100, 100, 28, 3)
        elif self.shooting == True:
            pyxel.circb(100, 100, 28, 10)
        pyxel.line(68, 100, 83, 100, 13)
        pyxel.line(117, 100, 132, 100, 13)
        pyxel.line(100, 68, 100, 83, 13)
        pyxel.line(99, 100, 101, 100, 10)
        pyxel.pset(100, 99, 10); pyxel.pset(100, 101, 10)



Start()
