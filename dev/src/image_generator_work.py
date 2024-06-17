import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os



class ImageGenerator:
    """
    テキストプロンプトから画像を生成するためのクラス。
    
    Attributes:
        model_id (str): 使用するStable DiffusionモデルのID。
        device (str): モデルを実行するデバイス（例: 'cuda' または 'cpu'）。
        pipeline (StableDiffusionPipeline): テキストから画像を生成するためのパイプライン。
    """
    def __init__(self, model_id: str = "CompVis/stable-diffusion-v1-4", device: str = "cpu"):
        """
        指定されたモデルとデバイスでImageGeneratorを初期化します。
        書いてもらいたいコード
        ①deviceの設定(基本的にcpuだが、自分のデバイスを使いたい人はそちらを使ってもかまわない)
        ②model_idの設定
        ③pipelineの設定
        
        Args:
            model_id (str): 使用するStable DiffusionモデルのID。今回は"CompVis/stable-diffusion-v1-4"を使用
            device (str): モデルを実行するデバイス。デフォルトはcpu。
        """
        

    def _load_model(self) -> StableDiffusionPipeline:
        """
        書いてもらいたいコード
        ①Stable Diffusionモデルをロード
        ②指定されたデバイスに転送
        
        Returns:
            StableDiffusionPipeline: テキストから画像を生成するためのパイプライン。
        """
       
        return pipeline

    def generate_image(self, prompt: str,num_inference_steps: int = 30) -> Image.Image:
        """
        テキストプロンプトから画像を生成します。
        
        Args:
            prompt (str): 画像を生成するためのテキストプロンプト。
            num_inference_steps: ステップ数
        
        Returns:
            Image.Image: 生成された画像。
        """
        return self.pipeline(prompt,num_inference_steps=num_inference_steps).images[0]

    def save_image(self, image: Image.Image, filepath: str) -> None:
        """
        生成された画像をファイルに保存します。
        
        Args:
            image (Image.Image): 保存する画像。
            filepath (str): 画像を保存するファイルパス。
        """
        image.save(filepath)

# テスト用メイン実行
if __name__ == "__main__":
    generator = ImageGenerator()
    prompt = "A scenic view of a mountain at sunrise"
    image = generator.generate_image(prompt)

    generator.save_image(image, f"./generated_image.png")
