// Client Side Form Validation is done with the Jquery Validate Plugin

// Custom validator methods for the app's specifications

// Uses Regex to define email format
$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /[a-z]+@[a-z]+\.[a-z]+/.test( value );
};
// Uses regex to ensure password includes at least one uppercase letter and one number
$.validator.methods.pass = function( value, element ) {
    return this.optional( element ) || /^(?=(.*[A-Z]){1,})(?=(.*[0-9]){1,}).{5,}$/.test( value );
};
// Uses regex to exclude special characters from username
$.validator.methods.user = function( value, element ) {
    return this.optional( element ) || /^(?=.*[a-z])\w{3,}$/.test( value );
};

// Calls the validate method on the registration form
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
    // Custom message for custom validator method
    messages: {
        password: {
            pass: "Please include the required characters",
        },      
    }
});

// Calls the validate method on the login form
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
    // Custom message for custom validator method
    messages: {
        password: {
            pass: "Password does not match the format",
        },      
    }
});

// Calls the validate method on the add stock Form
// No custom rules or messages are required
$('.add-stock-form').validate();