# Conversational-AI-Sales-Voice-Bot

<span>A simple conversational sales voice bot created by using OpenAI and ElevenLabs.</span>
<br> The Steps I have followed to create the Voice Bot are as follows - </br>
<br><b>Step 1:</b> Recording the voice from laptop/PC mic using sounddevice with the mentioned duration and sample rate. Saving the record sample into ".wav" format.</br>
<br><b>Step 2:</b> Transcribe the ".wav" file into text using OpenAI Whisper.</br>
<br><b>Step 3:</b> Once we receive the text from the above step, we pass that as our query/question to the LLM (OpenAI 3.5 turbo) and generating response in the form of text.</br>
<br><b>Step 4:</b> The response from LLM is converted into voice using ElevenLabs (which provides human - like voices with multiple flexibities).</br>

<br> <b> Main Tech Stack </b> </br>
Soundevice, OpenAI, Elevenlabs

