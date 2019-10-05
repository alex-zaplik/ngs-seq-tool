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

    for (let i = 0; i < files.length; i++) {
        let file = files[i];
        console.log(file);
        formData.append('files[]',  file);
    }
    formData.append("prefix", prefix);
    console.log(prefix);


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