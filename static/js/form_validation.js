$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /[a-z]+@[a-z]+\.[a-z]+/.test( value );
}
$.validator.methods.pass = function( value, element ) {
    return this.optional( element ) || /^(?=(.*[A-Z]){1,})(?=(.*[0-9]){1,}).{5,}$/.test( value );
}

$.validator.methods.user = function( value, element ) {
    return this.optional( element ) || /^(?=.*[a-z])\w{3,}$/.test( value );
}

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

$('.login-form').validate({
    // Validation Rules
    rules: {
        username: {
            required: true,
            user: true
        },
        password: {
            required: true,
            minlength: 5,
            pass: true,
        }
    },
    messages: {
        password: {
            pass: "Password does not match the format",
        },      
    }
});

$('.add-stock-form').validate()