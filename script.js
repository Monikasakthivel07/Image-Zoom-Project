document.addEventListener("DOMContentLoaded", function () {
    const startBtn = document.getElementById('start-btn');
    const container = document.querySelector('.container');
    const experience = document.getElementById('experience');
    const videoFeed = document.getElementById('video-feed');
    const zoomImage = document.getElementById('zoom-image');

    startBtn.addEventListener('click', async () => {
        container.style.display = 'none';
        experience.style.display = 'block';
        await startHandTracking();
    });

    async function startHandTracking() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoFeed.srcObject = stream;

            const hands = new Hands({ locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}` });
            hands.setOptions({
                maxNumHands: 1,
                modelComplexity: 1,
                minDetectionConfidence: 0.7, // Increased confidence for stability
                minTrackingConfidence: 0.7
            });

            hands.onResults((results) => {
                if (results.multiHandLandmarks.length > 0) {
                    const landmarks = results.multiHandLandmarks[0];

                    // Get thumb and index finger tips
                    const thumbTip = landmarks[4];
                    const indexTip = landmarks[8];

                    // Calculate distance
                    const distance = Math.sqrt(
                        Math.pow(thumbTip.x - indexTip.x, 2) +
                        Math.pow(thumbTip.y - indexTip.y, 2)
                    );

                    // Reduced zoom factor for stability
                    const scale = 1 + distance * 3; // Reduced from 5 to 3 for less sensitivity
                    zoomImage.style.transform = `translate(-50%, -50%) scale(${scale})`;
                }
            });

            function detectHands() {
                hands.send({ image: videoFeed }).then(() => {
                    requestAnimationFrame(detectHands);
                });
            }
            detectHands();

        } catch (error) {
            console.error("Error accessing webcam:", error);
            alert("Could not access webcam. Please check camera permissions.");
        }
    }
});
