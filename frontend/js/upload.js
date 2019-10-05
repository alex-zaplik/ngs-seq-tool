const url = 'process.php';
const form = document.querySelector('form');

document.getElementById('single').checked = true;

form.addEventListener('submit', e => {
    e.preventDefault();

    const files = document.querySelector('[type=file]').files;
    const formData = new FormData();

    let prefix = "double";
    if(document.getElementById('single').checked) {
        prefix = "single";
    }
    let runs = document.getElementById('runs').value;
    let samples = document.getElementById('samples').value;
    let i7Column = document.getElementById('i7').value;
    let i5Column = document.getElementById('i5').value;

    if (files.length === 0)
    {
        return;
    }

    for (let i = 0; i < files.length; i++) {
        let file = files[i];
        console.log(file);
        formData.append('files[]',  file);
    }
    formData.append("prefix", prefix);
    formData.append("runs", runs);
    formData.append("samples", samples);
    formData.append("i7", i7Column);
    formData.append("i5", i5Column);

    fetch(url, {
        method: 'POST',
        body: formData
    }).then(response => {
        console.log(response);
       window.location.href = "result.php";
    });
});

updateList = function() {
    var input = document.getElementById('file');
    var output = document.getElementById('fileList');

    for (var i = 0; i < input.files.length; ++i) {
        output.innerHTML += '<li>' + input.files.item(i).name + '</li>';
    }
}