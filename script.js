let startButton = document.getElementById("start");
let resetButton = document.getElementById("reset");
let input = document.getElementById("input");
let sentenceDisplay = document.getElementById("sentence");
let timeDisplay = document.getElementById("time");
let wpmDisplay = document.getElementById("wpm");
let accuracyDisplay = document.getElementById("accuracy");
let tabs = document.querySelectorAll(".tab");

let time = 0;
let started = false;
let sentence = "";
let interval;
let currentLevel = "beginner"; // default

// ===== TAB SWITCH =====
tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        tabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
        currentLevel = tab.getAttribute("data-level");
        resetTest();
        sentenceDisplay.textContent = `Selected ${currentLevel} level. Click 'Start' to begin.`;
    });
});

// ===== FETCH SENTENCE =====
async function loadSentence() {
    const res = await fetch(`/get_sentence/${currentLevel}`);
    const data = await res.json();
    sentence = data.sentence;
    sentenceDisplay.textContent = sentence;
}

// ===== START TEST =====
startButton.addEventListener("click", () => {
    loadSentence();
    input.value = "";
    input.disabled = false;
    input.focus();
    time = 0;
    started = false;
    clearInterval(interval);
    timeDisplay.textContent = 0;
    wpmDisplay.textContent = 0;
    accuracyDisplay.textContent = 0;

    interval = setInterval(() => {
        if (started) {
            time++;
            timeDisplay.textContent = time;
        }
    }, 1000);
});

// ===== HANDLE INPUT =====
input.addEventListener("input", () => {
    if (!started) started = true;

    let typed = input.value;
    let correctChars = 0;
    for (let i = 0; i < typed.length; i++) {
        if (typed[i] === sentence[i]) correctChars++;
    }

    let accuracy = ((correctChars / typed.length) * 100) || 0;
    accuracyDisplay.textContent = accuracy.toFixed(1);

    let wordsTyped = typed.trim().split(/\s+/).length;
    let wpm = Math.round((wordsTyped / time) * 60) || 0;
    wpmDisplay.textContent = wpm;

    if (typed === sentence) {
        clearInterval(interval);
        input.disabled = true;
        alert(`✅ Completed!\nLevel: ${currentLevel.toUpperCase()}\n⏱ Time: ${time}s\n💨 Speed: ${wpm} WPM\n🎯 Accuracy: ${accuracy.toFixed(1)}%`);
    }
});

// ===== RESET TEST =====
resetButton.addEventListener("click", resetTest);

function resetTest() {
    input.value = "";
    input.disabled = true;
    sentenceDisplay.textContent = "Select a level and click 'Start'.";
    time = 0;
    started = false;
    clearInterval(interval);
    timeDisplay.textContent = 0;
    wpmDisplay.textContent = 0;
    accuracyDisplay.textContent = 0;
}
