function populate_customer_status(data){
    x = document.getElementById("c_stat");
    // x.innerHTML = "<tr><th>Customer ID</th><th>Customer SSN ID</th><th>Status</th><th>Message</th><th>Last Updated</th><th>Operations</th><th>View Profile</th></tr>";
    x.innerHTML = data;
    // console.log(String(data));
    // <tr><td>John</td><td>Doe</td><td>john@example.com</td><td>John</td><td>Doe</td><td><a href='{{ url_for('customerStatus') }}'><u><b>Refresh</b></u></a></td><td><a href=''><u><b>View Details</b></u></a></td></tr>
}