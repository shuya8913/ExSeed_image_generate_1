## NvidiaのGPUを使いたい場合
### Nvidia Container Toolkitをインストール
ターミナル上で以下のコマンドを打つ(Windowsの方はwsl環境で行う)

1. 
```sh
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
```
2. 
```sh
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
3.
```sh
sudo apt-get update
```
4.
```sh
sudo apt-get install -y nvidia-container-toolkit
```
参考リンク: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
