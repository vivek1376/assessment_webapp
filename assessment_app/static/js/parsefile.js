document.addEventListener("DOMContentLoaded", function() {
    console.log("hello from parsefile.js!!!");

        document.getElementById("parsefileform").addEventListener('submit',
        function (event) {
            event.preventDefault();
            console.log("file submit button clicked!!");

            const formData = new FormData(document.getElementById("parsefileform"));

            axios.post('/parsefile', formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            }).then(function (response) {
                console.log(response);
            });
        });

});
