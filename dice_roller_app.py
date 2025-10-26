<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dice Roller</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom Keyframes for a simple rolling animation */
        @keyframes roll {
            0% { transform: rotateX(0deg) rotateY(0deg) scale(1); opacity: 1; }
            50% { transform: rotateX(180deg) rotateY(180deg) scale(0.9); opacity: 0.5; }
            100% { transform: rotateX(360deg) rotateY(360deg) scale(1); opacity: 1; }
        }

        /* Class to apply the animation */
        .rolling {
            animation: roll 0.5s ease-out 3; /* Runs 3 times */
        }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                }
            }
        }
    </script>
</head>
<body class="bg-gray-900 min-h-screen flex flex-col items-center justify-center p-4 font-sans">

    <div class="max-w-md w-full bg-gray-800 p-8 rounded-xl shadow-2xl text-center">
        <h1 class="text-3xl font-bold text-white mb-6">🎲 Dice Roller App 🎲</h1>

        <!-- Dice Display Area -->
        <div id="dice-container" 
             class="dice-display w-32 h-32 mx-auto mb-8 
                    flex items-center justify-center text-7xl font-extrabold 
                    bg-white text-gray-900 border-4 border-yellow-500 
                    rounded-2xl shadow-inner cursor-pointer select-none
                    transition-all duration-300 transform hover:scale-105"
             data-result="1">
            1
        </div>

        <!-- Result Text -->
        <p id="result-text" class="text-xl text-yellow-300 font-semibold mb-8">
            Click the button to roll!
        </p>

        <!-- Roll Button -->
        <button id="roll-button" 
                class="w-full py-3 px-6 
                       bg-yellow-600 hover:bg-yellow-500 
                       text-gray-900 font-bold text-lg 
                       rounded-xl shadow-lg transition duration-200 
                       transform active:scale-95 disabled:opacity-50">
            Roll the Dice!
        </button>
        
        <!-- API Call Simulation placeholder for complexity -->
        <div id="loading-indicator" class="hidden mt-4 text-sm text-yellow-400">Rolling...</div>
    </div>

    <script>
        // DOM Elements
        const diceContainer = document.getElementById('dice-container');
        const rollButton = document.getElementById('roll-button');
        const resultText = document.getElementById('result-text');
        const loadingIndicator = document.getElementById('loading-indicator');
        
        // Define number of sides for the dice
        const NUM_SIDES = 6;

        /**
         * Simulates a dice roll, updates the UI, and applies a visual effect.
         */
        function rollDice() {
            // Disable button and show loading for effect
            rollButton.disabled = true;
            loadingIndicator.classList.remove('hidden');

            // 1. Generate a random result
            const result = Math.floor(Math.random() * NUM_SIDES) + 1;

            // 2. Apply rolling animation
            diceContainer.classList.add('rolling');
            
            // 3. Wait for the animation to finish before showing the final result
            // The animation runs for 0.5s and repeats 3 times (1.5s total)
            const animationDuration = 1500; // 1.5 seconds

            setTimeout(() => {
                // Remove animation class
                diceContainer.classList.remove('rolling');
                
                // Update the display with the final result
                diceContainer.textContent = result;
                diceContainer.dataset.result = result; // Store result in data attribute

                // Update text
                resultText.textContent = `You rolled a: ${result}!`;

                // Re-enable button and hide loading
                rollButton.disabled = false;
                loadingIndicator.classList.add('hidden');
                
            }, animationDuration);
        }

        // --- Event Listeners ---
        rollButton.addEventListener('click', rollDice);
        diceContainer.addEventListener('click', rollDice);

        // Initial state update
        document.addEventListener('DOMContentLoaded', () => {
             // You can optionally add a small message or instruction here
        });

    </script>
</body>
</html>
