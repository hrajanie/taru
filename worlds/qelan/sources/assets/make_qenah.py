#!/usr/bin/env python3
# Qenʾah — a titling capital whose stroke-weight COOLS as it descends:
# thin/radiant at the top, heavy/settled at the foot; slab serifs only at the
# baseline (the iron floor). The cosmology of the Ladder, made into letterforms.
import math, base64

UPM   = 1000
CAP   = 700          # cap height
HW_TOP = 30.0        # half stroke-width at the radiant top
HW_BOT = 63.0        # half stroke-width at the settled foot
GAMMA  = 1.25        # how the cooling accelerates toward the floor
FOOT_W = 1.62        # foot slab half-width, x times bottom half-width
FOOT_H = 30          # foot slab height
LSB    = 46          # left side bearing
RSB    = 46          # right side bearing

def hw(y):
    t = max(0.0, min(1.0, y/CAP))
    t = t**GAMMA
    return HW_BOT + (HW_TOP - HW_BOT)*t

def area(c):
    s=0.0
    for i in range(len(c)):
        x0,y0=c[i]; x1,y1=c[(i+1)%len(c)]
        s += x0*y1 - x1*y0
    return s/2.0
def orient(c, ccw=True):
    return c if (area(c)>0)==ccw else c[::-1]

def normal(dx,dy):
    L=math.hypot(dx,dy) or 1.0
    return (-dy/L, dx/L)

def ribbon(points):
    """variable-width stroke -> closed CCW contour. width follows hw(y)."""
    n=len(points)
    seg=[normal(points[i+1][0]-points[i][0], points[i+1][1]-points[i][1]) for i in range(n-1)]
    vn=[]
    for i in range(n):
        if i==0: nx,ny=seg[0]
        elif i==n-1: nx,ny=seg[-1]
        else:
            ax,ay=seg[i-1]; bx,by=seg[i]; nx,ny=ax+bx,ay+by
            L=math.hypot(nx,ny) or 1.0; nx/=L; ny/=L
            # miter correction so width holds through the corner
            dot=ax*nx+ay*ny
            if abs(dot)>0.2: nx/=dot; ny/=dot
        vn.append((nx,ny))
    left=[]; right=[]
    for i,(x,y) in enumerate(points):
        w=hw(y); nx,ny=vn[i]
        left.append((x+nx*w, y+ny*w)); right.append((x-nx*w, y-ny*w))
    return orient(left+right[::-1], ccw=True)

def arc_pts(cx,cy,rx,ry,a0,a1,step=6.0):
    pts=[]; a=a0; d=step if a1>=a0 else -step
    while (a<=a1) if a1>=a0 else (a>=a1):
        r=math.radians(a); pts.append((cx+rx*math.cos(r), cy+ry*math.sin(r))); a+=d
    r=math.radians(a1); pts.append((cx+rx*math.cos(r), cy+ry*math.sin(r)))
    return pts

# ---- stroke emitters (append contours to C) ----
def stem(C,x,y0=0,y1=CAP,ft=True):
    C.append(ribbon([(x,y0),(x,y1)]))
    if ft and y0<=2: foot(C,x)
def bar(C,y,x0,x1):
    C.append(ribbon([(x0,y),(x1,y)]))
def diag(C,x0,y0,x1,y1):
    C.append(ribbon([(x0,y0),(x1,y1)]))
def arc(C,cx,cy,rx,ry,a0,a1):
    C.append(ribbon(arc_pts(cx,cy,rx,ry,a0,a1)))
def foot(C,x):
    w=hw(0)*FOOT_W; h=FOOT_H
    C.append(orient([(x-w,0),(x+w,0),(x+w,h),(x-w,h)], ccw=True))
def ring(C,cx,cy,r):
    outer=[]; inner=[]
    a=0
    while a<360:
        ra=math.radians(a); c=math.cos(ra); s=math.sin(ra)
        py=cy+r*s; w=hw(py)
        outer.append((cx+(r+w)*c, cy+(r+w)*s))
        inner.append((cx+(r-w)*c, cy+(r-w)*s))
        a+=6
    C.append(orient(outer, ccw=True))
    C.append(orient(inner, ccw=False))     # the counter (hole)
def dot(C,x,y,r):
    C.append(orient(arc_pts(x,y,r,r,0,354), ccw=True))

# ---------------- glyph skeletons (caps) ----------------
def G():  return []   # fresh contour list
LET = {}

def A():
    C=[]; diag(C,40,0,300,700); diag(C,560,0,300,700); bar(C,205,150,450); return C,600
def B():
    C=[]; stem(C,70); arc(C,70,525,335,178,90,-90); arc(C,70,178,375,178,90,-90); return C,530
def Cc():
    C=[]; arc(C,310,350,300,330,58,302); return C,580
def D():
    C=[]; stem(C,70); arc(C,70,350,430,350,90,-90); return C,580
def E():
    C=[]; stem(C,70); bar(C,683,70,470); bar(C,350,70,420); bar(C,18,70,475); return C,520
def F():
    C=[]; stem(C,70); bar(C,683,70,460); bar(C,372,70,415); return C,500
def Gg():
    C=[]; arc(C,310,350,300,330,55,305); bar(C,352,360,575); stem(C,575,82,352,ft=False); return C,600
def H():
    C=[]; stem(C,70); stem(C,500); bar(C,350,70,500); return C,570
def I():
    C=[]; stem(C,110); return C,220
def J():
    C=[]; C.append(ribbon([(330,700),(330,210),(322,120),(285,55),(205,28),(120,45),(70,110)])); return C,420
def K():
    C=[]; stem(C,70); diag(C,80,352,500,700); diag(C,80,352,520,0); return C,540
def L():
    C=[]; stem(C,70); bar(C,18,70,455); return C,490
def M():
    C=[]; stem(C,60,ft=True); stem(C,640,ft=True); diag(C,60,690,350,250); diag(C,640,690,350,250); return C,700
def N():
    C=[]; stem(C,70); stem(C,520); diag(C,70,700,520,0); return C,590
def O():
    C=[]; ring(C,320,350,278); return C,640
def P():
    C=[]; stem(C,70); arc(C,70,520,360,180,90,-90); return C,540
def Q():
    C=[]; ring(C,320,360,278); diag(C,360,210,575,10); return C,650
def R():
    C=[]; stem(C,70); arc(C,70,522,330,178,90,-90); diag(C,250,348,530,0); return C,560
def S():
    C=[]
    spine=[(432,572),(352,664),(250,688),(150,652),(100,560),(138,470),(250,400),
           (300,362),(352,324),(430,234),(412,118),(315,26),(198,16),(92,92)]
    C.append(ribbon(spine)); return C,540
def T():
    C=[]; bar(C,683,20,520); stem(C,270); return C,540
def U():
    C=[]
    C.append(ribbon([(70,700),(70,230)]+arc_pts(290,230,220,210,180,360)+[(510,700)]))
    return C,580
def V():
    C=[]; diag(C,40,700,300,30); diag(C,560,700,300,30); return C,600
def W():
    C=[]; diag(C,30,700,200,30); diag(C,200,30,400,540); diag(C,400,540,600,30); diag(C,600,30,770,700); return C,800
def X():
    C=[]; diag(C,50,700,520,0); diag(C,520,700,50,0); return C,570
def Y():
    C=[]; diag(C,50,700,290,360); diag(C,530,700,290,360); stem(C,290,0,360); return C,580
def Z():
    C=[]; bar(C,683,55,500); diag(C,495,675,60,25); bar(C,18,50,505); return C,555

LET = {'A':A(),'B':B(),'C':Cc(),'D':D(),'E':E(),'F':F(),'G':Gg(),'H':H(),'I':I(),
       'J':J(),'K':K(),'L':L(),'M':M(),'N':N(),'O':O(),'P':P(),'Q':Q(),'R':R(),
       'S':S(),'T':T(),'U':U(),'V':V(),'W':W(),'X':X(),'Y':Y(),'Z':Z()}

# punctuation / figures
def PERIOD():
    C=[]; dot(C,70,55,62); return C,200
def COMMA():
    C=[]; dot(C,80,70,62); C.append(ribbon([(80,40),(40,-120)])); return C,210
def HYPHEN():
    C=[]; bar(C,330,40,300); return C,360
def COLON():
    C=[]; dot(C,70,470,60); dot(C,70,120,60); return C,200
def EXCLAIM():
    C=[]; C.append(ribbon([(95,700),(95,210)])); dot(C,95,60,62); return C,210
def ONE():
    C=[]; stem(C,210); diag(C,90,560,210,690); return C,360
def TWO():
    C=[]; C.append(ribbon(arc_pts(250,490,200,200,170,-30))); diag(C,400,360,70,20); bar(C,18,70,470); return C,540
def THREE():
    C=[]; C.append(ribbon(arc_pts(250,520,185,185,150,-95))); C.append(ribbon(arc_pts(250,185,195,195,95,-150))); return C,520
def ZERO():
    C=[]; ring(C,270,350,225); return C,560
LET['.']=PERIOD(); LET[',']=COMMA(); LET['-']=HYPHEN(); LET[':']=COLON()
LET['!']=EXCLAIM(); LET['1']=ONE(); LET['2']=TWO(); LET['3']=THREE(); LET['0']=ZERO()

# ---------------- normalise: side bearings + advance ----------------
def bbox(C):
    xs=[p[0] for c in C for p in c];
    return (min(xs),max(xs)) if xs else (0,0)

GLYPHS={}; ADV={}
for ch,(C,w) in LET.items():
    if C:
        x0,x1=bbox(C)
        shift=LSB - x0
        C=[[(px+shift,py) for (px,py) in c] for c in C]
        adv=int(round((x1-x0)+LSB+RSB))
    else:
        adv=w
    GLYPHS[ch]=C; ADV[ch]=adv
ADV[' ']=300; GLYPHS[' ']=[]

# ===================================================================
def to_svg_path(C):
    d=""
    for c in C:
        d+="M "+" L ".join(f"{x:.1f} {y:.1f}" for x,y in c)+" Z "
    return d

def render_specimen(path):
    SC=0.10
    def line(text,x,y):
        out=""; cx=x
        for ch in text:
            C=GLYPHS.get(ch); adv=ADV.get(ch,300)
            if C:
                d=to_svg_path([[(px,CAP-py) for px,py in c] for c in C])
                out+=f'<path transform="translate({cx:.1f},{y:.1f}) scale({SC})" d="{d}" fill="#241c0f"/>'
            cx+=adv*SC
        return out,cx
    body=""
    # baseline floor rules + words
    rows=["THE CODEX","OF DEGREES","RADIANCE","QENAH","ABCDEFGHIJKLM","NOPQRSTUVWXYZ","0123 .,:-!"]
    yy=70
    for r in rows:
        s,endx=line(r,40,yy)
        body+=f'<line x1="38" y1="{yy+2}" x2="{endx+6:.0f}" y2="{yy+2}" stroke="#b89b6a" stroke-width="0.8"/>'
        body+=s; yy+=92
    W=1000; H=int(yy+20)
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="{W}" height="{H}" fill="#efe5cc"/>{body}</svg>'
    open(path,"w").write(svg)
    return W,H

def build_ttf(path):
    from fontTools.fontBuilder import FontBuilder
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    order=[".notdef"]+list(GLYPHS.keys())
    name_for={".notdef":".notdef"," ":"space",".":"period",",":"comma","-":"hyphen",
              ":":"colon","!":"exclam"}
    def gname(ch):
        if ch in name_for: return name_for[ch]
        if ch.isdigit(): return {"0":"zero","1":"one","2":"two","3":"three"}.get(ch,ch)
        return ch
    glyph_order=[".notdef"]+[gname(ch) for ch in GLYPHS]
    fb=FontBuilder(UPM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    cmap={ord(ch):gname(ch) for ch in GLYPHS}
    fb.setupCharacterMap(cmap)
    glyf={}; metrics={}
    pen=TTGlyphPen(None); glyf[".notdef"]=pen.glyph(); metrics[".notdef"]=(600,0)
    for ch,C in GLYPHS.items():
        pen=TTGlyphPen(None)
        for c in C:
            pen.moveTo((round(c[0][0]),round(c[0][1])))
            for p in c[1:]: pen.lineTo((round(p[0]),round(p[1])))
            pen.closePath()
        g=pen.glyph(); nm=gname(ch); glyf[nm]=g
        metrics[nm]=(ADV[ch], LSB if C else 0)
    fb.setupGlyf(glyf)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=760, descent=-180)
    fb.setupNameTable({"familyName":"Qenah","styleName":"Titling",
        "fullName":"Qenah Titling","psName":"Qenah-Titling",
        "version":"1.0","copyright":"Qelan / Sealed Radiance display face"})
    fb.setupOS2(sTypoAscender=760, sTypoDescender=-180, usWinAscent=760, usWinDescent=180)
    fb.setupPost()
    fb.font.save(path)

if __name__=="__main__":
    import sys, os
    here=os.path.dirname(os.path.abspath(__file__))
    render_specimen(os.path.join(here,"qenah-specimen.svg"))
    build_ttf(os.path.join(here,"Qenah-Titling.ttf"))
    b=open(os.path.join(here,"Qenah-Titling.ttf"),"rb").read()
    open(os.path.join(here,"Qenah-Titling.b64"),"w").write(base64.b64encode(b).decode())
    print("glyphs:",len(GLYPHS),"ttf bytes:",len(b))
