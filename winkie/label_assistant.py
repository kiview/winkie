# AUTOGENERATED! DO NOT EDIT! File to edit: 03_label_assistant.ipynb (unless otherwise specified).

__all__ = ['LabelAssistant']

# Cell
import os
import pandas as pd
from .dlc_importer import DLCImporter

class LabelAssistant:
    """Used to label data and generate labelled data."""

    def __init__(self, behaviors, data_path, default_label='not_defined'):
        self.behaviors = behaviors
        self.default_label = default_label
        self.files = os.listdir(data_path)
        self.file_paths = [os.path.join(data_path, f) for f in self.files]
        self.labels = {'behavior': [], 'start': [], 'end': [], 'file': []}
        self.imp = DLCImporter()

    def addLabel(self, behavior, start_frame, end_frame, file_name):
        if behavior not in self.behaviors:
            raise ValueError(f"Unknown behaviour: {behavior}")
        if file_name not in self.files:
            raise FileNotFoundError(file_name)

        # There might be a user error of labellig frames that are not existent in the specified file.
        # We decide to ignore this potential user error for now, since we don't want to initially load the files.

        self.labels['behavior'].append(behavior)
        self.labels['start'].append(start_frame)
        self.labels['end'].append(end_frame)
        self.labels['file'].append(file_name)

    def apply_labels(self):
        def import_and_tag(file_name):
            df = self.imp.import_hdf(file_name)
            df['file_name'] = os.path.basename(file_name)
            df['frame'] = df.index
            return df

        df_list = [import_and_tag(f) for f in self.file_paths]
        df_merged = pd.concat(df_list)
        df_merged['behavior'] = self.default_label

        for i, f in enumerate(self.labels['file']):
            file_name_select = df_merged['file_name'] == f
            frame_select = (self.labels['start'][i] <= df_merged['frame']) & (df_merged['frame'] <= self.labels['end'][i])
            df_merged.loc[file_name_select & frame_select, ['behavior']] = self.labels['behavior'][i]

        return df_merged

    def to_df(self):
        return pd.DataFrame(self.labels)