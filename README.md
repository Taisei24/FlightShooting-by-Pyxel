# FlightShooting-by-Pyxel
Python でレトロゲームを作成できるモジュール "Pyxel" を用いて、3Dのフライトシューティングゲームを作成しました。<br>
<br>
"FlightShooting.py" をダウンロードすることで、プレイできます。<br>
ゲームプレイには、"Pyxel" だけでなく "NumPy" が必要です。<br>


##  FLIGHT – SHOOTING 

↓こちらからコードを取得できます（GitHub）

<https://github.com/Taisei24/FlightShooting-by-Pyxel>



### **1\. ゲーム概要**

- 一人称視点で機体を操縦し、的を破壊するゲーム
- 全部で３つのステージがあり、的の個数や増え方が異なる
  - 1<sup>st</sup> stage は、的を１個破壊すると、新たに２個が生成され、５個を破壊するとステージクリア
  - 2<sup>nd</sup> stage は、的を１個破壊すると、新たに３個が生成され、10個を破壊するとステージクリア
  - 3<sup>rd</sup> stage は、的を１個破壊すると、新たに4個が生成され、20個を破壊するとステージクリア
- エースコンバットシリーズを参考にしたが、真似た部分はほとんどない
  - エースコンバットはロックオン形式だが、本作はロックオンを採用していない
  - エースコンバットはレーダーを表示するが、本作はワールドマップを表示する
  - エースコンバットは機体の操縦が複雑だが、本作は左右キーのみで操縦する

### **2\. 操作について**

- 機体の操縦：左右キー
  - 左右キーを用いて、機体の傾き（バンク角）を操作する
- 弾丸の発射：スペースキー
  - 弾丸の発射には、３つの制約がある
  - 1\. チャージ
    - 一度発射すると、次の発射までに時間がかかる
  - 2\. 発射時の機体の水平
    - 弾丸を発射するときは、機体が水平になっている必要がある
  - 3\. 発射後の機体の水平
    - 弾丸を発射した後は、しばらく機体の傾きがロックされる

### **3\. 画面について**

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAIAAAAP3aGbAAAdHElEQVR4Ae2dv64kx3WHZw3CjuyAgS2agP0AtCPFwkJPsYG9ICAwIx/BoSLHZEYYEFYO9ikEQrEAARRfQIBBK2HCTMmq9/5mr87dmqqp7q4/p6o+Ydjbt7r+nPOd4vSnnuHdZ5/89NPLjP/77ne/mjEtcoJAFoFZ/73+m6zs6QQBCEDAAYEJDQu3crCvCMEFgfk8C8NysbHaBMEqEBidwFSGhVuNvh2JvwaBmTwLw6qxQ5gTAhCoQmASw8KtquwOJh2XQBD5HJ6FYQWFpQECEPBKYHjDwq28bi3i8khgdM/CsDzuKmKCAARuEhjYsCq61U1UNEJgFgLjehaGNcseJA8ILEBgSMPCrRbYmaRYncCInoVhVd8WLOCbANGNRGAww8KtRtpcxDoCgbE8C8MaYU8RIwQg8EBgGMPCrR7qxQECVQiM4lknDasKOyaFAAQgcJPAAIaFW92sHI0QKE7Av2dhWMWLzoQQgEAtAq4NC7eqVfZD8zJoEQKePQvDWmQTkiYEZiDg1LBwqxk2FzmMTMCnZ2FYI+8pYodAJQJep3VnWLiV161CXCsS8OZZGNaKu5CcITAoAUeGhVsNuocIe3oCfjwLw6qw2ZgSAhCoQ8CFYeFWdYrLrBAoScCDZ2FYJSvKXBCAQFUCnQ0Lt6paXSavT2C5Ffp6Foa13IYjYQiMS6CbYeFW424aIodAL8/CsNh7EIDAMAQ6GJZxq2EwESgEIBASaO9ZGFZYBVogAAGnBJoaFm7ldBcQFgROEGjpWRjWiUIxdA8B+kLgPIFGhoVbnS8VM0DAM4E2noVhed4DxAYBCDwhUN2wcKsnvPkBAlMTuHpWtRwxrGpomRgCEChNoKJh4Vali8V8EBiDQD3PwrDG2AFECQEIbASqGBZutZE9/mIkBKYgUMOzMKwptgZJQGANAoUNC7daY9uQJQRyCZT1LAwrlzv9IFCBAFPuI1DMsHCrfeDpDYGVCJTyLAxrpV1DrhAYnEABw8KtBt8DhA+BRgTOe9bQhtWIMstAAAJOCJwyLNzKSRUJAwIDETjjWRjWQIUmVAisTuCgYeFWq2+c5vmz4GQEjnkWhjXZNiAdCMxMYLdh4VYzbwdyg0BbAns9C8NqWx9WgwAE7hKId9hhWLhVHCNXIACB4wTyPQvDOk6ZkRCAQGMCWYaFWzWuCstBYEECOZ6FYU23MUgIAvMSuGNYuNW8pSczCHgkkPYsDMtjzYgJAhC4SSBqWLjVTV40QsATgWljiXkWhjVtyUkMAvMRuGFYuNV8ZSYjCIxIIPQsDGvEOhIzBBYl8MSwFnOrRUtO2hAYi4D1LAxrrNoRLQSWJnA1LNxq6V1A8hBwT0CehWG5LxQBliDAHBCAAAQgAAEIQAACEIDATQKvv3mzvW5eohECEICAKwJZz7BcRUwwEIDAsgSeKXMrWS+eXxt1iSMEIAABJwQwLCeFIAwIQOA+gRsyhW3dxzZxD1KDgGMCGJbj4hAaBCDwlMANw7IdsC1Lg3MIQKAvAQyrL39Wh0BHAuMtfcewbELYlqXBOQQg0J4AhtWeOStCAAJtCWy2tb3arslqEIDA6gQwrMM7gIEQgEBrAjueYYWhWcni+/EhH1ogAIGyBDCssjyZDQIQqEjglGHZuLAtS4PzyQiQjhMCGJaTQhAGBCBwn0Axw7JLYVuWBucQgEApAhhWKZLMAwEIVCdQxbBs1K+/efP4I58kPqLgBAIQOEAAwzoAjSEQgEAfAtUNy6bFsy1Lg3MIQGAvAQxrLzH6JwlwEQI1CTQ1LJsItmVpcA4BCOQQwLByKNEHAhBwQaCbYdnssS1Lg3MIDEKgQ5gYVgfoLAkBCExCYLOt7TVJMqQBAQgUJYBhFcXJZBCAQE0CLp5hhQlayZr0+/Fh0rRAAAJ3CGBYdwBxGQIQ8EPAqWFZQNiWpcE5BFYmgGGtXH1yb0SAZUoRGMCwbKrYlqXBOQRWI4BhrVZx8oXAwAQGMyxLGtuyNDiHwAoEBjCsFcpAjhCAQA6BgQ3LpodtWRqcQ2BWAhjWrJUlLwhMSGASw7KVwbYsjcHOCRcCSQIYVhIPFyEAAQg0I7DZ1vZqthwLQQACVQlgWFXxMjkEIBAjcKR9wmdYIQYrWfzuh5APLRAYhQCGNUqliBMCELgsYVi2ztiWpcE5BMYigGGNVa/HaDmBwIoEljMsW2Rsy9LgHAL+CWBY/mtEhBCAwJXA0oZ1ZfDwB7b1gIGDRwLE9EgAw3pEwQkEIOCdAIZ1o0LY1g0oNEHAAQEMy0ERCAECEMgjML9h5XGI9sK2omi4AIHmBDCs5shZEAIQgEADApttba8GC7EEBCBwkwCGdRMLjWMSIOrZCfAMa3eFrWTxux9242MABE4QwLBOwGMoBCDQlgCGdYo3tnUKH4MhsJOAMaydI+kOAQhAoDEBDKsYcGyrGEomgkCEAIYVAUMzBCDgjwCGVaUm7m2rStZ20levXm0/vnz5cjvygkApAhhWKZLMAwEIVCfwQfUVllzAfj8L21pyC5B0FQIYVhWsTAoBPwRmioRnWE2rOZNt6SnVGXw84TpDb82xGNaadSdrCAxJAMPqVrZRbCtmUmk/0qicPmEB0qPC/rSsQwDDulNrLkMAAn4I8Clht1qEnyTall5hyYzs6vV8JzZzyxhsppz7J4Bh+a8REUIAAlcCGNYVRN8/5Fa9nmpZo4lZT0s+YQyNImyZJGsdIoBhHcLGIAhAoAcBDKsH9cia8ixdbGNbMpfQaBSDn6ONcJSY/dCbKRIMa6ZqkgsEJidQzrAmB9U6vXq2JUNRPtZc1OL/qJhHz8I/Z58RYlg+60JUEIDADQIY1g0o3ppK2ZasRIbiLce98dgsZsprL4fV+mNYq1W8SL5MAoE+BDCsPtwPr3rMtuZ2ENnW3Dke3jCTDcSwJiso6UBgZgIY1sDVzbGtdbwDz6q0lV1Ni2G5KgfBQAACKQIYVorOQNdC2/rzH3+9xf+3//Kf2/FyWeVvr8GzHso97QHDmra0JAaB+QhgWHVr2mV2uZVcQ25l/8tEG5L1Mts++rlyX+f53ej1yo8fw8pnRU8IQKAzAQyrcwHKLh9ziphJzW1eeFbZ3eVhNgzLQxWIYQoCJFGfAIZVn3GTFeRWez8TXMG88KwmG7DRIhhWI9AsAwEInCeAYZ1neGqGj776OjH++88/S1zVJbmVPOL1N/rWla4cP+41L60UG6WrfY/iY1n1jYfVjxFwY1jHwmcUBCCwEgEMq1u1026lsNQnx7P0eV9tx0nPrxgUuY4yvvQo9eQIgRwCGFYOJfpAAAIuCDxzEcViQcib9iYdepZ9IiO78ekyis3kez3tFa3ldg2FPwYhgGENUijChAAELpdnuvv1utddFvvfMbeykORZ1hHGraAit9npvM1utAy1Lkf/BDAs/zUiQggMTKBs6B/obha712kx9dE5RwiUIhDbV+zGUoTnmwfDmq+mZASBaQlkfUrIHa9U/c8/w/rvf/i7LRh9b3s72V6qTsxWtg6TvZRvmNQxAjzJCkl6bsGwPFfnQnAQgIAlkPVN9/S9q+wdzwbHeZqAyKerk55hxKuxfEUjzCjWP+xJi38CGJb/GhEhBCBwJZBlWNe+kT9id7DYHU/TxEbpKkcI7CUQ21Hpfajff793rSr9mTSDAIaVAYkuEICADwJZnxLWCDV934vdLWtE0n7OY58V8vlgjUppH8qz3v2+1rfrzL0D32Y45j8Y1ph1I2oILEmgm2Glaeu+F+tz4+4X6+q4Pd+zZvrvB30WJPw2VmwHzrH3fFYhJyoMK4cSfSAAARcECnxKWCOP9H0sdvdTJOmx6uPhKG9Ke5b6eIh2tRhiuyi292L9V+NWO18MqzZh5i9OgAnXJeDUsNIFSd/NxroH4lDpWnu7Gtt7sV2n+GOjdJVjPgEMK58VPSEAgc4EnH5KWIPKuPdA+xmWsuCOXWOHWM5l51fVwjmpY8jkvZb3fsSw3gPCjxCAgF8CQz7DOoYzfTeL3QO1Vnqs+nCEQIxAbP/Edl2sf2z+ddoxrHVqTaYQGJ7AQoaVrlX6nha7E2rO9Fj1OX9UDLvWOr8oM1QlEKumah0uHesf9py1BcOatbLkBYEJCWBYWUVN39li90NNnR6rPhwhYAnE9gw7DcOy+4RzCAxLYI3AMawCdY7dDzV17K6YHqWx4x7/9Nv/2IL/p5/973bkVYpAes+ssNMwrFJ7iXkgAIHqBBb6pnt1ljsXiN0PNY1+B6bOaxzt32xYdn65lZ2znmfpu+l2rbLn9SiVjTM9W2ynpX0tPWevqxjWA3kOEIDACAQwLKdVsndF2dZYd3t5Vj23qlE2+dpYnM9wsHvMzuPZvDAsWynOIQAB1wT4lNBpeexdTnd+ez+0V30m4NitfALrEFVsF9mdFoYVGxX2rNGCYdWgypwQgEAVAhhWFaw1JrV3NnsPtO011mXO1Qikd5Tde5ZMepTteeYcwzpDj7EQgEBTAnsNq2lwLBYjYO9m9o5n22NjaYfAGQKxPWb3oZ0/1t/2yT/HsPJZ0RMCEOhMAMPqXIDzy9s7mL3L2fbzqzADBNIEYvvN7slwhtiosKdaMCxx4HiDAE0Q8EaAb7p7q0g0Hn0bK/972PbOtvc+Fg1i0gt72U6KoUNadpfa5WM7FsOylDiHAARcE+AZluvynAnO3qPsfcy2n5mfsVMR6JRMbDfaHWtDw7AsDc4hAAHXBDAs1+UpFZy9j9l7l20vtRbzQOA8gdjOxLDOs2UGCECgEQEMqwTooeaw9y5sa6jSEewFw2ITQAACwxDge1jDlEqB1vvG0Jq2VY+n6sWxLAEMqyxPZpueAAn2JMAzrJ70Xa3Nsy1X5SCYmwQwrJtYaIQABDwSwLA8VqV7TKFt2Zbu4RHAsgQaG9aynEkcAhAoQIBPCQtAbD9F+8+25vsMsT3D9vtkvhUxrPlqSkYQmJYAz7CmLW3ZxOwzrEzbKhsAs0FgI4BhbRB4QQACYxDgGdYYdboZpYenMCPalgduNwtK410CGNZdRHSAAATuEWh1HcNqRbraOn58wb9t+WFVbTtMPjGGNXmBSQ8CMxHgU8KZqtk5Fz5J7FyABZbHsBwUmRAgAIE8AjzDyuPkvpfnpzMenm155uN+czkKEMNyVAxCgQAE0gQwrDSfwa7694j2tuWMyWA7ylu4GJa3ihAPBCAQJYBhRdGMe2EUp6htW6NwGHentY8cw2rPnBUhAIGDBMYyrINJrjlsLL8oa1tj5b7m/jyWNYZ1jBujIACBDgQwrA7QWy45omucsa0R8225H0ZfC8MavYLTxk9iEAgJYFghkwlbxvWOfNsaN8cJN1y1lDCsamiZGAIQgAAEDhPYHGR7HR7efeBmW9srDGNLanuF7bQMQyA7UAwrGxUdIQCB3gR4htW7As3XtzLy8uXL5uufXVCS9ec//vpxohGzeAyek10EMKxduOgMAQj0JIBh9aRfZu0Ts8i2xjIUG7NsSwDs7ztVC8f5CGBY89WUjCAwLQEMa9rS5icmZ1F/n7aVEyG2pQrOfcSw5q4v2U1GYPV0MKzVd8B7+VuX0aX2znU+BmxLtZvviGHNV1MygsC0BDCsaUtbKrHQdzTzefOqN7Mi1BHbEoc5jksZ1hwlIwsIrEsAw1q39iczj/lR/rTnHS1/LfXEtsRh3COGNW7tiBwCyxHAsJYr+SIJ300T27qLyGEHDMthUQgJAhC4TQDDus2F1qUIYFujlBvDGqVSxAkBCFxuGxZgILAsAWzLc+kxLM/VITYIQOAJAQzrCQ5+gIAlgG1ZGh7OMSwPVegaA4tDAAIQgMBkBDbb2l6TJTVcOhjWcCUjYAisS4BnWOvWnswPELCSNeBvkT+Qsa8hGJavehANBCCQIIBhJeBwCQIpAthWik6daxhWHa7MCgEIVCCAYeVDpScEogSwrSiaohcwrKI4mQwCEKhJAMOqSZe5lySAbdUrO4ZVjy0zD0yA0H0SwLCy6vLJTz/N6kcnCBwl8N3vfnV06ELjMKyFik2qEBidAIYVrSBWFUXDhcoEsK0Y4CqGFVuMdghAAAJnCGBYT+hhVU9w8IMDAtiWLQKGZWlwDgEIuCaAYV2wqlM7lMENCWBbGFbD7cZSEIDAOQKLGhZWdW7bMLo/gTVtC8Pqv/OIAAKDEOgf5kKGhVX1325EUIfAOraFYdXZQcwKAQhUIDC5YWFVFfYMU7omMLdtYVjNNh8LQQACZwlMaFgerOr1//39VpkXH/+4HWu/5r6jlqXnYW+UzSg923x7A8NKV5yrEICAIwIfOIrlRCh975w37mM/+WLLJmzvG+cWEq82BJysYvdbuBudBLkrDAxrFy46QwACPQkM/AzL3j1aIix7pzqfhY3H/jbxlkw8r/Xi+V83+XnanjPNj83umfxRHnpiWB6qQAwQgEAWAY/PsBKB971D1rgvac6yeVmnSMCc/hK+GSux3W/agbGe3toxLG8VIR4IQCBKYADDsneDaB6VL9S+C2l+D5lWBsn07gjYXad96C5EExCGZWBw2p4AK0JgDwGnhmXf9fekU75vy3uO1vKTe3mazOibQLj3tCf9RI1h+akFkUAAAncIuDCs8H39TtRNLve6t2hdn0yagGcRRwTsPtTOPBFcgaEYVgGITAEBCLQh0M2w7Dt3m1TzVzl2J3n16lViiZcvXyauhpcUg2dKYcy0zE3A7kbtz/b5YljtmbMiBCBwkEBTw7Lv0AfjrTxs733DWlXaofJ72hQVzwM32+z0/KOvvn4vsu8//+y9Fn6cg4Ddk9qlbfLCsNpwZhUIQKAAgeqGZd+JC8TrZgoZU9qqbLC2596xdh6f56FbKU6141miMevR/jte27YwrFl3EXkNTIDQYwSqGJZ9x40tPG77eT+SbZ2fZ1yGRD4rAfvvfg3bwrBm3TnkBYEJCRQzLPvOOiKnGneDUhwU2+iES9FgnlEI2B2rPXw+8gkN6zwUZoAABHwSOGVY9h3UZ3ployr71GmmJ1n6HFCfCVrmarctnK9JwL5XnLEtDGvN/UPWEBiSwG7Dsu+UQ2ZM0NUIdPCparkcm/iMOxxb8fyo9v9G2xX3EsOwzlecGSAAgUYEsgzLviM2iqv5Mn/4yRePa/7b/3/5eH7s5Ntf/nwb+O//9ZvteOZlo3px+fHMVIztQkDPPbW0fWqpFh3VrnP1ty22Xee6qp5q0VHtOo8dNSqnZ2yGsu32vSXHtjCssvyZDQIQqETg7bRRw7LvfG87zv7PeauyhORW5z3LRvXJx5/aJTh3TiDmMrKb8KptiZ2HKWu2sD1s0Zxhu58W+54Tsy0My0+9iAQCELhD4Ilh2Xe4O+O4DAEIJAnIfeQ1Ok92v15U/+sP5g/bbmeLtZuh11ONsv2vF1z+Yd+LrG1hWC7LVT4oZoTADAQ+sO9kMyRUMwd7j9J5erX0kyzd63LmSa/CVc8EVN/8Wtv+Nq90u+0537l9j8Kw5qsvGUFgWgJPnmH5zNL+P1hFqG8n2U/Q1G7fidWSf9TYcK38GWI9054VG2XbFZtt4dw/AVmV4pQf6XzvUWPtbHYG266el8vFdpjsHMOarKCkA4GZCTzzdvdOO47cyhYk9Cx7dW926dXtzLqz7b2n6ZtZv//XX2xT5Y9NZ2Fjfv3Nm23mF8+fbUdeIY00yfPEbC3Oz9ZmhtpMymaBYZXlyWwQgEBFAi6eYdW7L9mZM+8kmbDlR/IsDVGLzsOjev7+4UK650MXDkMSKLvHhkRQOWgMqzJgpocABMoR6GxY1oDSSYVPr9Rf7eknWeqptdL3QF1VT41KH60ryaFi/W1PPcnSp4ex/mpXPDrnCAEIYFjsgYUJkPpoBLoZVr7FlEWqddPmoqvqmb+6daj0KLlV2rMUQ3oerkJgNQIY1moVJ18IDEygg2HtNRc9pUozVp+cJ1maRzGkLUZX1VOj2hy1bpu10qvIAW0fuaFtmfU8v+62XvmjZuVm87JkbPuZ8xOGdWZZxkIAAhDYT6CpYR27/+R70970FU/6PqCr6rl3/nR/2YosRudaKz2qzVVFFa6ldkUbXp2vReYeyytnZ+qz4/znm+FamkHt4Ty6Grar/95j2dn2rp7TH8PKoUQfCEDABYFGhlXDUErxU2xpu9FV9Sy1ruaRrWh+tbg8EtRBAqH7yGI0Xc5V9bGjNFZHXdW5jrZn/lU7SvP4PGJYPutCVBCAwA0CjQzrxsoDNsmDcjxLzz5ynnFozgFhEHIWAZlLaDpqsVftedbUD51io9Lza9TDBBed2/5q93nEsHzWhagg0I2A54WrG1aOj3gApDhzfCfso7E5WYRjc0a176Mna/pM0K6udtvC+VgErE+NFbmixbDEgSMEIDAAgeqGpac5IpHzTEc9xzqG3vTi8uOWwuh/VzM+tRWx2St8ihS2nPEjO5udx7Y3S/bwQhjWYXS3B9IKAQjUI1D9d7rb5zvWtpSSN+cKXUlxej5awuFvMfccee3YQhr59bVU03HaOfNHpeec46olUyojDKsUSeaBAASqE6j4DCu824Q+ZZ0rvFo9+2ABxVzjzhAsRYNrAll7IMjg2KhgGhqiBDCsKBouQAAC3ghUNKycVK1VWdvSWHtVLRwhAIGVCWBYK1ef3CEwGIGmhvXkm9MBqDeX795r+/by863l2ZefbEe95FyaJ/yWkNrVM/8YzpM/lp4QgEBLAhhWS9qsBQEInCLQ1LD2uoyMSValLNXyj8//eftR5+GcYcvWuchLnyEWmerAJHwCdQDa4SH5tbZ1yR91OLCBBloypcLGsEqRZJ4EAS5BoAyBpoa1N2S5kjWpsEWfLb754u3zr3dPu36zd6HD/X/44Ydt7Icffrgdc162v87tqPx57CjO6xH46KuvE5N///lnias1Ltn/BrDG/P7nxLD814gIIQCBKwHXhiW3ukZq/pBnqUFPuPR54psHz/rDl1/o0nbU1e2k+Cv0o2NLYFXHuI0ySk6kaPV7EXR+pt3OoDk1m851teOx6tIYVlW8TA4BCJQk4MiwQp+yJpVO2vb89pd/7Svzevds6217KeeSGeV7lnpq1Ns43v0Ta393ffU/w6dI7Z8cHatBzHpsu841v85lSTpPt+vqakcMa7WKky8EBiZQ0bD0LYz0N1OsVVlLOkM0nMc6l33CpVWscylmtZc6xhzK2tZjn1KLTjBP6FZKSu2jeJZiDo9yKPlUeDWnRWM1T07/OfpgWHPUkSwgsASBioaVwy+0oZxRe/s8XeX9b2npm1yaU7+LXee1j7IqrWJtSy0cZyVgzUh+pBYd1WJzj7WrT/qq+sx0xLBmqia5DEWAYPcT6GxY+wMuP+LJM6yPP921QI4ZxfrE2ncFQOeqBM48KZP7xMKLXd3bLiOLjYqtPm47hjVu7YgcAssRqP635oho+rNC9el7rPH5YJuMLNvw74lpE0O9VfSZoJ0/33pCGuNW2RJY+XxYw1q5aOQOgVUJ8Axr1coPkne+T3lI6Idf/MxDGE5i+PB/fls8EgyrOFImhAAEahFoZFh6dmCfttRKaP+8im3/OEY0I8BCELgSwLCuIPgDAhDwT6CRYQmEXMaPZykexcYRAucJ1Hhqcz6qmWbAsGaqJrlAYHgC6QSaGpZCkdf09SzFoHg4QgACoxDAsEapFHFCAAKXDoYl6nKc9p6ldRUDRwhAYCwCGNZY9boTLZchMDeBboYlrPKdNp6ltbQuRwhAYEQCGNaIVSNmCCxKoLNhibp1n7K2ZWfWWisc9VsKVsh06RyXTB7DWrLsJA2BMQm4MCyLLnSifOcKx9qZVzh/8fzZCmmS47IEMKxlS0/iEBiPgDvDChFW8aZwGVogAAH3BDAs9yUiQAhA4B2BRr/T/d1y/AkBCEDgOAEM6zg7Rg5CgDDnIcAb1jy1JBMITE+AN6zpS0yCEJiHAG9Y89SSTCAwPYG7b1jTEyBBCEBgGAJ/AZ+ZrnrTTiDSAAAAAElFTkSuQmCC)


- コックピットから見えるワールド
  - ①：ワールド（壁・ターゲット・弾丸）が、一人称視点で描画される。
- コックピット内の情報
  - ②：照準器。射撃可能な状態であれば、照準円の内側に緑色の円が描画され、射撃可能であることを分かりやすくパイロットに伝える。また、壁やターゲットに近づきすぎると、警告 “WARNING” が表示される。
  - ③：水準器。気体の傾きをパイロットに伝える。
  - ④：コンパス（方向指示器）。マップ上での機体の進行方向を示す。
  - ⑤：「すでに破壊したターゲットの個数／ステージクリアに必要なターゲット数」
  - ⑥：マップ。ワールド情報をパイロットに伝える。自分の機体は、黄色で描画される。
  - ⑦：ステージ情報
  - ⑧：機体が水平か否かを示す。傾いていれば “inclined” が表示され、赤色に点灯する。水平であれば “horizontal” が表示され、緑に点灯する。発射後、傾きがロックされている状態であれば “rocked” が表示され、黄色に点灯する。
  - ⑨：弾丸発射についてのチャージが完了しているかどうかを示す。チャージ中であれば “charging” が表示され、赤色に点灯する。完了していれば “ready” が表示され、緑に点灯する。発射中と発射後の数フレームは “shooting” が表示され、黄色に点灯する。さらに、文字の下側にチャージメーターがついており、チャージ状況を把握することができる。

### **4\. プレイのシーケンスについて**

（画像略）

- ①：スタート画面
  - スペースキーを押すと、ゲームが開始する。画面下側に、操作方法（USER GUIDE）が表示される。
- ②：ステージ開始時の遷移画面
  - ステージ開始前に表示される画面。18フレーム後、自動でゲームが開始する。ステージ番号と、そのステージで倒すべきターゲットの個数が示される。
- ③：ゲーム画面
  - 機体を操縦し、弾丸を発射して、規定の個数のターゲットを破壊する。
- ④：ステージクリア画面
  - スペースキーを押すと、次のステージに移行する。その際、②の遷移画面も表示される。
- ⑤：ゲームクリア画面
  - スペースキーを押すと、最初からリスタートする。
- ※：ゲームオーバー画面
  - スペースキーを押すと、ゲームオーバーになったステージをリトライできる。

### **5\. クリア条件**

- STAGE 1
  - ターゲットを５個破壊する
- STAGE 2
  - ターゲットを10個破壊する
- STAGE 3
  - ターゲットを20個破壊する

### **6\. ゲームオーバー条件**

- 機体が壁にぶつかる
- 機体がターゲットにぶつかる

### **7\. コードの解説**

#### **7.0. モジュールのインポート** # line 1~2

- このゲームは、pyxel だけではなく numpy を必要とする

#### **7.1. class Music():** # line 4~192

- BGMと効果音を定義しているクラス
  - BGMは３つのチャンネルで演奏され、残り１つのチャンネルで効果音が演奏される
- BGMは、およそ1分でループする
  - ロックマン２の「おっくせんまん」と、UNDERTALEの「MEGALOVANIA」に触発され、作曲した
  - 曲全体の構成は、ロックマンに類似している。すなわち、①リズミカルなパート、②メロディアスなパート、③ベースがカッコいいパート、④移行局面、の４つが循環する
  - コード進行は、MEGALOVANIAに類似している。ベースラインが「A, G, F#, F」と下降していくなかで、同じメロディーフレーズが繰り返される。
- ゲーム中の効果音は、①弾丸発射、②ターゲット爆破、③機体激突（ゲームオーバー）、の３つを用意した。
  - ノイズ音源を効果的に使い、それっぽい音を再現
- ゲームクリアの効果音も用意した

#### **7.2. class Start():** \# line 194~222

- このファイルが実行されたときに最初に呼び出されるクラス
- 画面を作ったり、音楽を定義したりなどの初期設定
- スペースキーを押すと、遷移画面を経て、ステージ1が始まる

#### **7.3. class Game_Over():** # line 224~250

- ゲームオーバーのときに呼び出されるクラス
- スペースキーを押すと、ゲームオーバーになったステージをリトライする

#### **7.4. class Next_Stage():** # line 252~280

- ステージ１またはステージ２をクリアしたときに呼び出されるクラス
- スペースキーを押すと、次のステージに進む

#### **7.5. class Game_Clear():** # line 282~306

- ステージ３をクリアしたときに呼び出されるクラス
- ゲームクリアの効果音が演奏される
- スペースキーを押すと、ステージ１からリスタート

#### **7.6. class Fighter():** # line 308~509

- このゲームの心臓部
- 行列演算を繰り返し、一人称視点からのワールド（壁）を描画する
  - ① 二次元のワールドを、４つの頂点で管理
    - ワールドの定義 # line 314
  - ② そのワールドにおいて、機体が移動する
    - 機体情報の定義 # line 310~313
      - tx：x座標, ty：y座標, dir：進行方向, bank：傾き
    - 機体の移動 # line 323~351
      - プレイヤーが操作するのは、機体の傾き（bank）のみ。他はすべて従属変数となる
      - プレイヤーは機体の進行方向を直接操作できず、傾きを操作することによる間接的な操作になるため、「機体の重さ」が感じられる
  - ③ 機体の座標を原点に、機体の向きをx軸の正として、４つの頂点座標を変換
    - 変換行列を作成 # line 356
    - ワールドの頂点座標を変換 # line 361
  - ④ 一人称視点で、いくつの頂点が見えるのかで場合分け
    - 毎フレーム、リストを作成 # line 322
    - それぞれの頂点の余弦を計算し、0.554以上（片側視野56.36度, y=±1.5xに相当）であればリストに格納していく # line 362~369
    - 以下、そのリストの要素数によって場合分けを行う
      - 頂点が0個見える場合 # line 371~389
      - 頂点が1個見える場合 # line 393~425
      - 頂点が2個見える場合 # line 427~448
      - 頂点が3個見える場合 # line 450~470
  - ⑤ 二次元ワールドにおける一人称視点は、「奥行の情報を持った一次元」となる
  - ⑥ 奥行の情報から「高さ」を作り出し、一次元を二次元に拡張する
    - 機体からの「奥行」と、機体から見える「高さ」が反比例するように計算
  - ⑦ 新たな行列を作成し、スクリーン上の頂点座標（原点中心・無回転）を格納していく
    - “self.scr” という行列をフレームごとに作成し、計算結果を格納していく
      - フレームごとに作成する理由は、フレームごとに表示する頂点の数が異なるため
  - ⑧ 機体の傾きに合わせた回転行列をかける # line 472~475
  - ⑨ スクリーンの左上が原点になるように平行移動させる # line 476
  - ⑩ 頂点の計算結果を行列から取り出し、直線を描いていく # line 479~509

#### **7.7. class Bullet():** \# line 512~542

- 弾丸の情報を管理するクラス
- インスタンスは常に12個存在し、“self.flag” によって存在するかどうかが判別される
- 弾丸はワールド座標上を移動し、それが壁に接触すると消滅する
- また、ターゲットに接触すると、弾丸は消滅し、ターゲットは爆発を開始する

#### **7.8. class Target():** # line 544~621

- ターゲットの情報を管理するクラス
- class Fighter の座標変換行列を流用して、ターゲットの座標を、ワールドの絶対座標から、機体を原点とした相対座標に変換する
- ターゲットの「奥行」の情報から、視点におけるターゲットの大きさを計算して描画する
- 弾丸が接触すると、爆発フェーズに入る
- コックピットから見えないターゲットについては、画面外に描画される
- 爆発局面において、新たにターゲットが生成される
  - def build(self, App): # line 606~621
  - ステージによって、異なる個数が生成される # line 581~595
  - 関数の再帰呼び出しによって、「座標のランダム性」と「機体との非接触」を両立

#### **7.9. class App():** \# line 624~809

- 実際にゲームを動かすクラス
- インスタンス生成時に、ステージ番号 “stage_num” を引数として受け取り、ステージに応じてゲームが進行する
- 弾丸発射にかかる３つの制約（「2. 操作について」を参照）は、このクラスで管理される
- コックピットの計器類の描画は、すべてこのクラスで行われる
  - def draw_cockpit(self): # line 730~809