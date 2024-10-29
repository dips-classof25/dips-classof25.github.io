document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.message-card');
    const delayBetweenMessages = 250; // Delay in milliseconds
	
    messages.forEach((message, index) => {
        setTimeout(() => {
            message.classList.add('hidden');
            message.classList.add('show'); // Add the "show" class to trigger CSS animation
        }, (messages.length - index) * delayBetweenMessages); // Stagger each message based on its index
    });
});