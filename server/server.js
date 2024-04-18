const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());


const mysql = require('mysql2'); 
const connection = mysql.createConnection({
  host: 'db.redhawks.us',
  user: 'redhawks_tax', 
  password: 'd2FPT24980y0',
  database: 'redhawks_tax'
});
connection.connect((err) => 
{
  if (err) {
    console.log("Error connecting to the database", err);
  }else {
    console.log("Connected to the database!");
  }
})

 
app.get('/', (req, res) => {
    const sql = 'SELECT Min, Max, HeadHousehold, Single, MarriedSeperately, MarriedJointly FROM Tax'; 
    connection.query(sql, (err, data) => {
        if (err) return res.json(err);  
        return res.json(data); 
      })
})

app.get('/income_single', (req, res) => {
  const sql = 'SET @var1 = 10;'
  + 'SELECT Single FROM `Tax` WHERE @var1 >= Min AND @var1 < Max';
  connection.query(sql, (err, data) => {
    if (err) return res.json(err);  
    return res.json(data); 
})

app.listen(2200, () => {
    console.log(`Server running on port 2200.`)
})

/*https://www.irs.gov/pub/irs-prior/i1040tt--2023.pdf*/