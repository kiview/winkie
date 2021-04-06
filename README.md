# Winkie
> AI/ML based behaviour classification of pigeon cooridnate data.


This file will become your README and also the index of your documentation.

## Install

`pip install winkie`

## How to use

You can import stuff and transform it!

```
imp = DLCImporter()
df = imp.import_hdf('example_data/coordinates.h5')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>bodyparts</th>
      <th colspan="3" halign="left">head</th>
      <th colspan="3" halign="left">beak</th>
      <th colspan="3" halign="left">left_neck</th>
      <th>right_neck</th>
      <th>...</th>
      <th>right_middle_wing</th>
      <th colspan="3" halign="left">right_down_wing</th>
      <th colspan="3" halign="left">body</th>
      <th colspan="3" halign="left">tail</th>
    </tr>
    <tr>
      <th>coords</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>...</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>773.376465</td>
      <td>231.518768</td>
      <td>0.999999</td>
      <td>726.495178</td>
      <td>235.638046</td>
      <td>0.999981</td>
      <td>726.502014</td>
      <td>277.634125</td>
      <td>0.999998</td>
      <td>803.271179</td>
      <td>...</td>
      <td>0.999998</td>
      <td>866.702393</td>
      <td>446.583923</td>
      <td>0.999997</td>
      <td>804.008545</td>
      <td>350.669586</td>
      <td>0.999992</td>
      <td>874.878601</td>
      <td>485.749908</td>
      <td>0.999999</td>
    </tr>
    <tr>
      <th>1</th>
      <td>773.129822</td>
      <td>231.487213</td>
      <td>0.999999</td>
      <td>725.662231</td>
      <td>235.242844</td>
      <td>0.999951</td>
      <td>725.964478</td>
      <td>278.003082</td>
      <td>0.999999</td>
      <td>803.197144</td>
      <td>...</td>
      <td>0.999997</td>
      <td>866.877441</td>
      <td>446.645325</td>
      <td>0.999989</td>
      <td>802.684265</td>
      <td>345.021454</td>
      <td>0.999873</td>
      <td>875.375854</td>
      <td>487.185547</td>
      <td>0.999997</td>
    </tr>
    <tr>
      <th>2</th>
      <td>773.009827</td>
      <td>231.793518</td>
      <td>0.999999</td>
      <td>726.025696</td>
      <td>235.272522</td>
      <td>0.999978</td>
      <td>725.764893</td>
      <td>278.884918</td>
      <td>0.999998</td>
      <td>802.567810</td>
      <td>...</td>
      <td>0.999997</td>
      <td>867.120056</td>
      <td>447.921356</td>
      <td>0.999995</td>
      <td>801.531067</td>
      <td>349.937347</td>
      <td>0.999946</td>
      <td>876.269714</td>
      <td>485.816010</td>
      <td>0.999999</td>
    </tr>
    <tr>
      <th>3</th>
      <td>773.748779</td>
      <td>231.791260</td>
      <td>0.999999</td>
      <td>726.288940</td>
      <td>235.864319</td>
      <td>0.999985</td>
      <td>725.889465</td>
      <td>279.045715</td>
      <td>0.999998</td>
      <td>803.356934</td>
      <td>...</td>
      <td>0.999992</td>
      <td>866.839966</td>
      <td>448.009460</td>
      <td>0.999994</td>
      <td>802.792908</td>
      <td>350.675842</td>
      <td>0.999970</td>
      <td>875.973022</td>
      <td>485.560150</td>
      <td>0.999998</td>
    </tr>
    <tr>
      <th>4</th>
      <td>774.934326</td>
      <td>231.623734</td>
      <td>0.999999</td>
      <td>726.298279</td>
      <td>235.749908</td>
      <td>0.999990</td>
      <td>726.302551</td>
      <td>278.388367</td>
      <td>0.999999</td>
      <td>802.530273</td>
      <td>...</td>
      <td>0.999995</td>
      <td>866.429382</td>
      <td>446.349670</td>
      <td>0.999998</td>
      <td>803.659973</td>
      <td>351.269745</td>
      <td>0.999938</td>
      <td>876.481873</td>
      <td>485.140839</td>
      <td>0.999998</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>691.788513</td>
      <td>232.490265</td>
      <td>1.000000</td>
      <td>673.796082</td>
      <td>238.801743</td>
      <td>0.018886</td>
      <td>697.399841</td>
      <td>282.134796</td>
      <td>0.999998</td>
      <td>737.725342</td>
      <td>...</td>
      <td>0.999993</td>
      <td>866.965027</td>
      <td>433.505768</td>
      <td>0.999980</td>
      <td>788.017456</td>
      <td>337.912994</td>
      <td>0.999999</td>
      <td>882.997253</td>
      <td>483.786896</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>96</th>
      <td>691.545410</td>
      <td>232.707413</td>
      <td>1.000000</td>
      <td>673.634888</td>
      <td>238.658234</td>
      <td>0.016135</td>
      <td>697.256165</td>
      <td>283.058899</td>
      <td>0.999999</td>
      <td>736.505920</td>
      <td>...</td>
      <td>0.999995</td>
      <td>868.164307</td>
      <td>432.291901</td>
      <td>0.999943</td>
      <td>788.334045</td>
      <td>339.911743</td>
      <td>0.999999</td>
      <td>884.470215</td>
      <td>483.485382</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>97</th>
      <td>691.117371</td>
      <td>232.242767</td>
      <td>1.000000</td>
      <td>673.748840</td>
      <td>239.055954</td>
      <td>0.007289</td>
      <td>696.269043</td>
      <td>282.351929</td>
      <td>0.999999</td>
      <td>735.976685</td>
      <td>...</td>
      <td>0.999984</td>
      <td>868.530457</td>
      <td>434.697205</td>
      <td>0.999916</td>
      <td>785.626465</td>
      <td>338.561829</td>
      <td>0.999997</td>
      <td>885.270691</td>
      <td>485.053131</td>
      <td>0.999999</td>
    </tr>
    <tr>
      <th>98</th>
      <td>691.294067</td>
      <td>232.225220</td>
      <td>1.000000</td>
      <td>673.927002</td>
      <td>239.141891</td>
      <td>0.004682</td>
      <td>695.629456</td>
      <td>282.407013</td>
      <td>1.000000</td>
      <td>735.639404</td>
      <td>...</td>
      <td>0.999977</td>
      <td>868.368958</td>
      <td>434.125732</td>
      <td>0.999876</td>
      <td>786.011963</td>
      <td>338.520691</td>
      <td>0.999997</td>
      <td>885.585388</td>
      <td>484.755859</td>
      <td>0.999999</td>
    </tr>
    <tr>
      <th>99</th>
      <td>691.483643</td>
      <td>232.269226</td>
      <td>1.000000</td>
      <td>673.797241</td>
      <td>239.390625</td>
      <td>0.010126</td>
      <td>695.367371</td>
      <td>281.720947</td>
      <td>0.999999</td>
      <td>735.199585</td>
      <td>...</td>
      <td>0.999970</td>
      <td>868.662292</td>
      <td>434.387238</td>
      <td>0.999786</td>
      <td>785.282776</td>
      <td>338.077087</td>
      <td>0.999992</td>
      <td>885.361023</td>
      <td>483.480896</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 36 columns</p>
</div>


To prepare the data for the further machine learning steps, we will change the coordinates to be relative to the body and rotate the coordinates, so that the vector between the body and the middle of the neck is orthogonal to the y-axis.

```
df = winkie.dlc_importer.transform_to_relative(df, 'body')
df = winkie.dlc_importer.add_middle_neck(df)
df = winkie.dlc_importer.add_rotation(df)
df = winkie.dlc_importer.apply_rotation(df)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>bodyparts</th>
      <th colspan="3" halign="left">head</th>
      <th colspan="3" halign="left">beak</th>
      <th colspan="3" halign="left">left_neck</th>
      <th>right_neck</th>
      <th>...</th>
      <th>right_down_wing</th>
      <th colspan="3" halign="left">body</th>
      <th colspan="3" halign="left">tail</th>
      <th colspan="2" halign="left">middle_neck</th>
      <th>rotation_angle</th>
    </tr>
    <tr>
      <th>coords</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>...</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th>likelihood</th>
      <th>x</th>
      <th>y</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-24.756667</td>
      <td>120.508710</td>
      <td>0.999999</td>
      <td>19.177848</td>
      <td>137.378264</td>
      <td>0.999981</td>
      <td>37.599212</td>
      <td>99.638046</td>
      <td>0.999998</td>
      <td>-37.599212</td>
      <td>...</td>
      <td>0.999997</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999992</td>
      <td>-4.411014</td>
      <td>-152.478855</td>
      <td>0.999999</td>
      <td>-1.421085e-14</td>
      <td>89.158479</td>
      <td>-116.026775</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-25.508326</td>
      <td>114.511197</td>
      <td>0.999999</td>
      <td>18.443110</td>
      <td>132.829171</td>
      <td>0.999951</td>
      <td>37.685982</td>
      <td>94.642246</td>
      <td>0.999999</td>
      <td>-37.685982</td>
      <td>...</td>
      <td>0.999989</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999873</td>
      <td>0.187954</td>
      <td>-159.670477</td>
      <td>0.999997</td>
      <td>0.000000e+00</td>
      <td>83.503899</td>
      <td>-117.149092</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-24.669384</td>
      <td>119.007761</td>
      <td>0.999999</td>
      <td>19.299872</td>
      <td>135.928651</td>
      <td>0.999978</td>
      <td>38.162277</td>
      <td>96.605391</td>
      <td>0.999998</td>
      <td>-38.162277</td>
      <td>...</td>
      <td>0.999995</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999946</td>
      <td>-9.546297</td>
      <td>-154.782895</td>
      <td>0.999999</td>
      <td>7.105427e-15</td>
      <td>87.485969</td>
      <td>-115.283267</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-25.269855</td>
      <td>119.743642</td>
      <td>0.999999</td>
      <td>19.277590</td>
      <td>136.612289</td>
      <td>0.999985</td>
      <td>38.326491</td>
      <td>97.857522</td>
      <td>0.999998</td>
      <td>-38.326491</td>
      <td>...</td>
      <td>0.999994</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999970</td>
      <td>-7.593725</td>
      <td>-153.269178</td>
      <td>0.999998</td>
      <td>-3.552714e-14</td>
      <td>88.193103</td>
      <td>-115.645195</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-26.205736</td>
      <td>120.223085</td>
      <td>0.999999</td>
      <td>19.378876</td>
      <td>137.673975</td>
      <td>0.999990</td>
      <td>37.930796</td>
      <td>99.283034</td>
      <td>0.999999</td>
      <td>-37.930796</td>
      <td>...</td>
      <td>0.999998</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999938</td>
      <td>-7.305264</td>
      <td>-152.220668</td>
      <td>0.999998</td>
      <td>-2.842171e-14</td>
      <td>90.176009</td>
      <td>-115.797288</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>-5.439143</td>
      <td>142.633716</td>
      <td>1.000000</td>
      <td>11.807338</td>
      <td>150.765213</td>
      <td>0.018886</td>
      <td>25.405257</td>
      <td>103.331178</td>
      <td>0.999998</td>
      <td>-25.405257</td>
      <td>...</td>
      <td>0.999980</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999999</td>
      <td>34.718510</td>
      <td>-170.572513</td>
      <td>1.000000</td>
      <td>1.421085e-14</td>
      <td>100.388462</td>
      <td>-134.573393</td>
    </tr>
    <tr>
      <th>96</th>
      <td>-5.111411</td>
      <td>144.342239</td>
      <td>1.000000</td>
      <td>11.891120</td>
      <td>152.534492</td>
      <td>0.016135</td>
      <td>25.831407</td>
      <td>104.212114</td>
      <td>0.999999</td>
      <td>-25.831407</td>
      <td>...</td>
      <td>0.999943</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999999</td>
      <td>30.892145</td>
      <td>-170.003613</td>
      <td>1.000000</td>
      <td>-7.105427e-15</td>
      <td>102.665676</td>
      <td>-134.105164</td>
    </tr>
    <tr>
      <th>97</th>
      <td>-4.902319</td>
      <td>142.167785</td>
      <td>1.000000</td>
      <td>12.372827</td>
      <td>149.214393</td>
      <td>0.007289</td>
      <td>25.929811</td>
      <td>102.332530</td>
      <td>0.999999</td>
      <td>-25.929811</td>
      <td>...</td>
      <td>0.999916</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999997</td>
      <td>28.892545</td>
      <td>-174.796723</td>
      <td>0.999999</td>
      <td>-1.421085e-14</td>
      <td>100.767981</td>
      <td>-133.609448</td>
    </tr>
    <tr>
      <th>98</th>
      <td>-5.977148</td>
      <td>142.247955</td>
      <td>1.000000</td>
      <td>11.306788</td>
      <td>149.369812</td>
      <td>0.004682</td>
      <td>25.838286</td>
      <td>103.199445</td>
      <td>1.000000</td>
      <td>-25.838286</td>
      <td>...</td>
      <td>0.999876</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999997</td>
      <td>30.290261</td>
      <td>-174.304594</td>
      <td>0.999999</td>
      <td>-2.131628e-14</td>
      <td>101.112080</td>
      <td>-134.109740</td>
    </tr>
    <tr>
      <th>99</th>
      <td>-6.258121</td>
      <td>141.260104</td>
      <td>1.000000</td>
      <td>11.399601</td>
      <td>148.452320</td>
      <td>0.010126</td>
      <td>25.362818</td>
      <td>103.041361</td>
      <td>0.999999</td>
      <td>-25.362818</td>
      <td>...</td>
      <td>0.999786</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.999992</td>
      <td>29.300697</td>
      <td>-174.067206</td>
      <td>1.000000</td>
      <td>-3.552714e-14</td>
      <td>100.597551</td>
      <td>-134.093794</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 39 columns</p>
</div>


## Development


This project uses [nbdev](https://github.com/fastai/nbdev) for development.
A regular workflow involves running the following commands in order:

```bash
nbdev_build_lib
nbdev_test_nbs
nbdev_build_docs
```

We also provide a convenient wrapper script:
```
./nbdev_build.sh
```

### Development Environment

The development environment can be created using [pipenv](https://pypi.org/project/pipenv/).
A corresponding `Pipfile` is provided, check the *Pipenv* documentation on how to use it.

There are a couple of tools pre-installed, such as Jupyter, etc..

Besides installing the development environment, the actual dependencies are managed by `nbdev` through Python's `setuptools` and defined in the `settings.ini` file, under the `requirements` key. 
In order to install them into your environment (ideally the environment created by *Pipenv*), just use the regular `setuptools` facilities:
```
pip install -e .
```
