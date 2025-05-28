from aiflipbook import FluxPipeline, LlamaStoryGen, FlipbookRenderer

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