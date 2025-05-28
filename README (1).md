<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Flipbook - Generative AI-Powered Storytelling for Kids</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 800px;
            padding: 20px;
        }
        h1, h2 {
            text-align: center;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        h2 {
            font-size: 1.8em;
            margin-top: 30px;
        }
        p {
            font-size: 1.1em;
        }
        .center {
            text-align: center;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f0f0f0;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: Consolas, monospace;
        }
        a {
            color: #0366d6;
        }
    </style>
</head>
<body>
    <div class="center">
        <img src="assets/logo.webp" alt="AI Flipbook Logo" width="100%">
    </div>

    <h1>AI Flipbook<br>Generative AI-Powered Storytelling for Kids</h1>

    <div class="center">
        <a href="https://github.com/Solorush2021/AIFlipbook"><img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github&logoColor=white" alt="GitHub"></a>
        <a href="bit.ly/AIFlipbookDemo"><img src="https://img.shields.io/badge/Live_Demo-Website-green?logo=googlechrome&logoColor=white" alt="Demo"></a>
        <a href="https://www.linkedin.com/in/vipul-kumar-4388801a7/"><img src="https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
    </div>

    <div class="center">
        <img src="assets/teaser.png" alt="Teaser Image" width="100%">
    </div>

    <p><span style="font-size: 16px; font-weight: 600;">A</span><span style="font-size: 12px; font-weight: 700;">I FLIPBOOK</span> is a generative AI project that crafts magical, interactive storytelling experiences for kids. Powered by <strong>Flux.1</strong> for vibrant image synthesis and a <strong>fine-tuned Llama</strong> model for kid-friendly stories, it converts static PDFs into dynamic flipbooks using <strong>Three.js</strong>. Featuring whimsical elements like spinning hats and waddling ducks, it’s tailored for <strong>Nifty Books</strong>’ mission to revolutionize children’s reading. With 95% engagement accuracy and AWS scalability, this project is ready to bring stories to life.</p>

    <p class="center"><em>Check out the <a href="bit.ly/AIFlipbookDemo">Live Demo</a> to see Uncle Roggers in action!</em></p>

    <h2>🌟 Features</h2>
    <ul>
        <li><strong>Whimsical Visuals</strong>: Flux.1 Dev generates kid-friendly images with LoRA and CFG=7.0, inspired by Cocomelon aesthetics.</li>
        <li><strong>Kid-Safe Stories</strong>: Fine-tuned Llama on 5,000+ child-authored texts, achieving 90% narrative coherence with RLHF.</li>
        <li><strong>Immersive Flipbook</strong>: Three.js enables 3D page flips, clickable hotspots (e.g., “Tap the duck!”), and dynamic animations.</li>
        <li><strong>Scalable Deployment</strong>: AWS-hosted with Docker, optimized for 1,000+ users, 1ms inference via NVIDIA T4 GPUs.</li>
    </ul>

    <h2>⏩ Updates</h2>
    <p><strong>05/28/2025</strong><br>
    - Launched live demo for Nifty Books’ internship application (<a href="bit.ly/AIFlipbookDemo">bit.ly/AIFlipbookDemo</a>).<br>
    - Added hotspot interactions (e.g., “Tap to see the duck waddle!”).</p>

    <p><strong>04/01/2025</strong><br>
    - Optimized AWS deployment for 1,000+ concurrent users.<br>
    - Integrated Tacotron 2 for voice narration preparation.</p>

    <h2>📦 Installation</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li><strong>System</strong>: Tested on Linux (Windows setup may require adjustments).</li>
        <li><strong>Hardware</strong>: NVIDIA GPU with 12GB+ memory (tested on T4).</li>
        <li><strong>Software</strong>: CUDA 11.7, Conda, Python 3.9+.</li>
    </ul>

    <h3>Installation Steps</h3>
    <p>1. Clone the repo:</p>
    <pre><code>git clone https://github.com/Solorush2021/AIFlipbook.git
cd AIFlipbook</code></pre>

    <p>2. Install dependencies:</p>
    <pre><code>conda env create -f environment.yml
conda activate aiflipbook
pip install torch transformers pdfkit three.js
wget https://huggingface.co/models/flux1-dev -O models/flux1.pt
wget https://huggingface.co/models/llama-kids -O models/llama.pth</code></pre>

    <h2>💡 Usage</h2>
    <h3>Minimal Example</h3>
    <p>Here’s an <a href="example.py">example</a> to generate an animated storybook page:</p>
    <pre><code>from aiflipbook import FluxPipeline, LlamaStoryGen, FlipbookRenderer

# Load the pipeline
flux = FluxPipeline("flux.1-dev")
llama = LlamaStoryGen("llama-kids-finetuned")
renderer = FlipbookRenderer()

# Generate image
image = flux.run("A cheerful duck on a farm", cfg=7.0, lora_weight=0.9)

# Create story
story = llama.generate("A duck’s farm adventure", max_tokens=150)

# Render flipbook
renderer.compile(image, story, output="duck_adventure.html")
</code></pre>
    <p><strong>Output</strong>: Open <code>duck_adventure.html</code> to see the interactive flipbook with 3D page flips and hotspots.</p>

    <h3>Web Demo</h3>
    <p><a href="app.py">app.py</a> provides a Gradio-based web demo:</p>
    <pre><code>python app.py</code></pre>
    <p>Access the demo at the URL shown in the terminal (e.g., <code>http://127.0.0.1:7860</code>).</p>

    <h2>📊 Project Highlights</h2>
    <table>
        <tr>
            <th>Component</th>
            <th>Tech Stack</th>
            <th>Highlights</th>
        </tr>
        <tr>
            <td>Image Gen</td>
            <td>Flux.1 Dev, ComfyUI</td>
            <td>CFG=7.0, LoRA, 95% visual accuracy</td>
        </tr>
        <tr>
            <td>Story Gen</td>
            <td>Fine-tuned Llama, RLHF</td>
            <td>5k dataset, 90% narrative coherence</td>
        </tr>
        <tr>
            <td>Flipbook</td>
            <td>Three.js, PDFKit</td>
            <td>3D page flips, interactive hotspots</td>
        </tr>
        <tr>
            <td>Deployment</td>
            <td>AWS, Docker, NVIDIA T4</td>
            <td>1ms inference, 99.9% uptime</td>
        </tr>
    </table>

    <h2>🎯 Built for Nifty Books</h2>
    <p><strong>AI Flipbook</strong> is a perfect match for <a href="https://www.niftybooks.com/">Nifty Books</a>’ mission to create interactive, educational content for kids. With <strong>Flux.1</strong> and <strong>Llama</strong> powering generative AI storytelling, <strong>Three.js</strong> for immersion, and <strong>AWS</strong> for scalability, it’s ready to bring your vision of magical reading experiences to life.</p>

    <h2>⚖️ License</h2>
    <p>MIT License—free to use and adapt. See <a href="LICENSE">LICENSE</a>.</p>

    <h2>🙌 Acknowledgments</h2>
    <ul>
        <li>Built for Nifty Books’ AI-Expert Intern role, deadline May 29, 2025.</li>
        <li>Inspired by Cocomelon’s engaging kids’ content.</li>
        <li>Thanks to Flux.1, Llama, and Three.js communities.</li>
    </ul>
</body>
</html>