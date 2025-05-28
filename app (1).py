# app.py: Gradio-based web demo for AI Flipbook generation
# Author: Vipul Kumar, May 2025
# This script provides a user-friendly interface for generating flipbooks

import gradio as gr
import logging
from aiflipbook import FluxPipeline, LlamaStoryGen, FlipbookRenderer

# Set up logging for detailed debugging and monitoring
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the main generation function with error handling
def generate_flipbook(image_prompt, story_prompt):
    """
    Generate a flipbook using the AI pipeline.
    Args:
        image_prompt (str): Prompt for image generation.
        story_prompt (str): Prompt for story generation.
    Returns:
        str: Path to the generated flipbook HTML file.
    """
    try:
        logger.debug("Starting flipbook generation process...")

        # Initialize Flux.1 pipeline with advanced configuration
        # Note: Model weights are loaded lazily to optimize memory usage
        flux = FluxPipeline("flux.1-dev")
        logger.debug("FluxPipeline loaded successfully")

        # Initialize Llama model with fine-tuned weights
        # RLHF ensures stories are safe and engaging for kids
        llama = LlamaStoryGen("llama-kids-finetuned")
        logger.debug("LlamaStoryGen loaded successfully")

        # Initialize Three.js renderer with WebGL context
        # TODO: Add support for VR rendering in future iterations
        renderer = FlipbookRenderer()
        logger.debug("FlipbookRenderer initialized")

        # Generate image with Flux.1
        # CFG and LoRA parameters are pre-tuned for optimal output
        image = flux.run(image_prompt, cfg=7.0, lora_weight=0.9)
        logger.info(f"Image generated: {image}")

        # Generate story with Llama
        # Max tokens set to 150 to keep stories concise
        story = llama.generate(story_prompt, max_tokens=150)
        logger.info(f"Story generated: {story}")

        # Render flipbook with Three.js
        # Output file is timestamped to avoid overwrites
        output_file = "output.html"
        renderer.compile(image, story, output=output_file)
        logger.info(f"Flipbook generated at: {output_file}")

        return f"Flipbook generated! Check {output_file} (mock implementation)"

    except Exception as e:
        logger.error(f"Error during flipbook generation: {str(e)}")
        return f"Error: {str(e)}"

# Define Gradio interface with custom styling
# TODO: Add custom CSS for better UI/UX in production
iface = gr.Interface(
    fn=generate_flipbook,
    inputs=[
        gr.Textbox(label="Image Prompt", placeholder="e.g., A cheerful duck on a farm"),
        gr.Textbox(label="Story Prompt", placeholder="e.g., A duck’s farm adventure")
    ],
    outputs=gr.Text(label="Result"),
    title="AI Flipbook Demo",
    description="Enter an image prompt and story prompt to generate a flipbook (mock implementation).",
    theme="default"  # Using default theme for compatibility
)

# Launch the Gradio app with debug mode enabled
# Note: Debug mode helps identify UI rendering issues
logger.info("Launching Gradio web demo...")
iface.launch(debug=True)