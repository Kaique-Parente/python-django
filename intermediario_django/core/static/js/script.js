function updateFileName(input) {
    const fileNameDisplay = document.getElementById('file-name');
    const fileSizeDisplay = document.getElementById('file-size');
    const icon = document.getElementById('upload-icon');

    if (input.files && input.files.length > 0) {
        const file = input.files[0];

        fileNameDisplay.innerText = file.name;
        fileNameDisplay.classList.remove('text-gray-500');
        fileNameDisplay.classList.add('text-[#092e20]', 'font-bold');

        const sizeInMB = (file.size / (1024 * 1024)).toFixed(2);
        fileSizeDisplay.innerText = `${sizeInMB} MB`;
        fileSizeDisplay.classList.remove('hidden');

        icon.classList.remove('text-gray-400');
        icon.classList.add('text-green-600');
    } else {
        fileNameDisplay.innerText = "Clique para fazer o upload";
        fileNameDisplay.classList.add('text-gray-500');
        fileSizeDisplay.classList.add('hidden');
        icon.classList.add('text-gray-400');
    }
}
