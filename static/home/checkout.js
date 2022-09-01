$(document).ready(function(){
    $('.payWithRazorpay').click(function (e){
        e.preventDefault();

        

        
        
            $.ajax({
                method:'GET',
                url:"/payment/proceed-to-pay",
                
                success:function(response){
                    console.log(response);

                }
            });

        var options = {
            "key": "rzp_test_EHJnISgTdTzYsc", // Enter the Key ID generated from the Dashboard
            "amount": "{{ amount }}", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "{{ currency }}",
            "name": "Coffee Corp",
            "description": "Test Transaction",
            "image": "https://example.com/your_logo",
            "order_id": "{{ razorpay_order_id }}", //This is a sample Order ID. Pass the `id` obtained in the response of Step 2
            "callback_url": "{{ callback_url }}",
            "prefill": {
            "name": "Gaurav Kumar",
            "email": "gaurav.kumar@example.com",
            "contact": "9999999999"
            },
            "notes": {
            "address": "Razorpay Corporate Office"
            },
            "theme": {
            "color": "#3399cc"
        }
        };
        var rzp1 = new Razorpay(options);
        
        rzp1.open();
    

        
    });
});