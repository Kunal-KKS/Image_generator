
import os
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--share', action='store_true')
    parser.add_argument('--always-high-vram', action='store_true')
    args = parser.parse_args()
def getImageFromPath(prompt):
    from modules.async_worker import worker, AsyncTask, async_tasks
    from modules import async_worker
    x=[False, prompt, '', ['Fooocus V2', 'Fooocus Enhance', 'Fooocus Sharp'], 'Hyper-SD', '1152×896 <span style="color: grey;"> ∣ 9:7</span>', 1, 'jpeg', '0', False, 2, 4, 'juggernautXL_v8Rundiffusion.safetensors', 'None', 0.5, True, 'sd_xl_offset_example-lora_1.0.safetensors', 0.1, True, 'None', 1, True, 'None', 1, True, 'None', 1, True, 'None', 1, False, 'uov', 'Disabled', None, [], None, '', None, False, True, False, False, 1.5, 0.8, 0.3, 7, 2, 'dpmpp_2m_sde_gpu', 'karras', 'Default (model)', -1, -1, -1, -1, -1, -1, False, False, False, False, 64, 128, 'joint', 0.25, False, 1.01, 1.02, 0.99, 0.95, False, False, 'v2.6', 1, 0.618, False, False, 0, False, False, 'fooocus', None, 0.5, 0.6, 'ImagePrompt', None, 0.5, 0.6, 'ImagePrompt', None, 0.5, 0.6, 'ImagePrompt', None, 0.5, 0.6, 'ImagePrompt', False, 0, False, None, False, 'Disabled', 'Before First Enhancement', 'Original Prompts', False, '', '', '', 'sam', 'full', 'vit_b', 0.25, 0.3, 0, False, 'v2.6', 1, 0.618, 0, False, False, '', '', '', 'sam', 'full', 'vit_b', 0.25, 0.3, 0, False, 'v2.6', 1, 0.618, 0, False, False, '', '', '', 'sam', 'full', 'vit_b', 0.25, 0.3, 0, False, 'v2.6', 1, 0.618, 0, False]
    async_result=AsyncTask(x)
    async_tasks.append(async_result)
    response=worker()
    print(async_worker.async_tasks,"kunal-------------------------------------------------------------------")
    print("img res",response)
    return response[0]


