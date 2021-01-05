# Winkie
> AI/ML based behaviour classification of pigeon cooridnate data.


This file will become your README and also the index of your documentation.

## Install

`pip install winkie`

## How to use

You can import stuff!

```python
imp = DLCImporter()
imp.import_hdf('example_data/coordinates.h5')
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
      <th>b1</th>
      <th colspan="3" halign="left">b2</th>
      <th colspan="3" halign="left">b3</th>
      <th colspan="3" halign="left">b4</th>
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
      <td>0.999986</td>
      <td>731.942932</td>
      <td>212.751831</td>
      <td>0.999972</td>
      <td>637.101440</td>
      <td>275.546967</td>
      <td>0.999044</td>
      <td>720.761475</td>
      <td>260.645416</td>
      <td>0.004323</td>
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
      <td>0.999984</td>
      <td>732.492004</td>
      <td>212.608414</td>
      <td>0.999969</td>
      <td>636.351440</td>
      <td>274.908783</td>
      <td>0.999068</td>
      <td>720.861084</td>
      <td>260.821045</td>
      <td>0.003748</td>
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
      <td>0.999989</td>
      <td>732.367859</td>
      <td>212.449570</td>
      <td>0.999967</td>
      <td>636.567993</td>
      <td>275.915558</td>
      <td>0.999465</td>
      <td>721.077087</td>
      <td>261.231415</td>
      <td>0.003017</td>
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
      <td>0.999988</td>
      <td>732.378052</td>
      <td>212.362946</td>
      <td>0.999962</td>
      <td>636.978821</td>
      <td>276.222534</td>
      <td>0.999626</td>
      <td>721.093933</td>
      <td>261.198242</td>
      <td>0.004915</td>
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
      <td>0.999991</td>
      <td>732.364014</td>
      <td>212.297073</td>
      <td>0.999969</td>
      <td>637.059021</td>
      <td>276.169647</td>
      <td>0.999717</td>
      <td>720.964783</td>
      <td>260.974213</td>
      <td>0.003497</td>
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
      <td>0.999981</td>
      <td>729.320374</td>
      <td>214.642715</td>
      <td>0.999988</td>
      <td>636.506165</td>
      <td>275.310120</td>
      <td>0.999486</td>
      <td>742.268372</td>
      <td>243.916214</td>
      <td>0.001441</td>
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
      <td>0.999983</td>
      <td>729.624817</td>
      <td>215.617279</td>
      <td>0.999986</td>
      <td>636.087585</td>
      <td>275.022858</td>
      <td>0.999226</td>
      <td>741.823853</td>
      <td>243.833771</td>
      <td>0.001208</td>
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
      <td>0.999982</td>
      <td>729.727722</td>
      <td>214.848831</td>
      <td>0.999987</td>
      <td>636.203613</td>
      <td>275.289307</td>
      <td>0.999269</td>
      <td>741.812866</td>
      <td>243.337326</td>
      <td>0.000828</td>
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
      <td>0.999983</td>
      <td>729.409668</td>
      <td>214.924347</td>
      <td>0.999989</td>
      <td>636.108765</td>
      <td>274.952759</td>
      <td>0.999238</td>
      <td>987.140259</td>
      <td>601.538696</td>
      <td>0.000869</td>
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
      <td>0.999981</td>
      <td>729.390991</td>
      <td>215.064926</td>
      <td>0.999983</td>
      <td>636.145447</td>
      <td>274.386780</td>
      <td>0.999225</td>
      <td>742.091919</td>
      <td>245.363281</td>
      <td>0.000920</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 60 columns</p>
</div>


