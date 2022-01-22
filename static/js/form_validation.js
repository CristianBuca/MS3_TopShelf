$('.reg-form').validate({
// Validation Rules
rules: {
    username: {
        required: true,
        user: true
    },
    email: {
        required: true,
        email: true
    },
    password: {
        required: true,
        minlength: 5,
        pass: true,
    },
    password_check: {
        required: true,
        equalTo: '#password'
    }
    },
    messages: {
        password: {
        pass: "Please include the required characters",
       },      
    }
});
