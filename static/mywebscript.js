
async function runEmotionDetection() {
    const text = document.getElementById("textToAnalyze").value;
    const resultElement = document.getElementById("system_response");

    if (!text.trim()) {
        resultElement.textContent = "Invalid text! Please try again!";
        return;
    }

    resultElement.textContent = "Analyzing...";

    try {
        const response = await fetch(
            `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`
        );

        const result = await response.text();
        resultElement.textContent = result;
    } catch (error) {
        resultElement.textContent =
            "Unable to connect to the emotion detection server.";
    }
}
