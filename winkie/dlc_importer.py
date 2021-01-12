# AUTOGENERATED! DO NOT EDIT! File to edit: 00_dlc_importer.ipynb (unless otherwise specified).

__all__ = ['DLCImporter', 'PigeonAnimator', 'PigeonAnimatorFactory']

# Cell
import pandas as pd

class DLCImporter:
    """Used to import DLC result files."""

    def import_hdf(self, file):
        df = pd.read_hdf(file)
        df.columns = df.columns.droplevel(0) # drop redundant scorer
        return df

# Cell
import matplotlib
import matplotlib.pyplot as plt

plt.rc('animation', html='jshtml')

class PigeonAnimator:
    """Animates a pigeon skeleton using matplotlib"""

    def __init__(self, skeleton, figsize=(10,6), xlim=(0, 1000), ylim=(0, 1000)):
        self.skeleton,self.figsize,self.xlim,self.ylim = skeleton,figsize,xlim,ylim

    def visualize(self, df, start, end):
        fig = plt.figure(figsize=self.figsize)
        ax = plt.axes(xlim=self.xlim, ylim=self.ylim)
        anim_bones = [ax.plot([], [], lw=2)[0] for _ in self.skeleton]

        def animate(i):
            data = df.iloc[[i]]

            for s, b in zip(self.skeleton, anim_bones):
                b.set_data([data[s[0],'x'], data[s[1],'x']], [data[s[0],'y'], data[s[1],'y']])

        plt.close()

        anim = matplotlib.animation.FuncAnimation(fig, animate, frames=range(start, end))
        return anim

# Cell
class PigeonAnimatorFactory:
    DEFAULT = PigeonAnimator([('left_neck', 'right_neck'), ('head', 'left_neck'), ('head', 'right_neck'), ('left_neck', 'tail'), ('right_neck', 'tail'),
                             ('left_neck', 'left_up_wing'), ('left_up_wing', 'left_middle_wing'), ('left_middle_wing', 'left_down_wing'), ('left_up_wing', 'left_down_wing'),
                             ('right_neck', 'right_up_wing'), ('right_up_wing', 'right_middle_wing'), ('right_middle_wing', 'right_down_wing'), ('right_up_wing', 'right_down_wing')])