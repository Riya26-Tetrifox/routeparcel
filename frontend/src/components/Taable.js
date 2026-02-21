export default function Taable({ taable,setTaable }) {
  const getDepartment=(weight)=>{
    if(weight<=1) return "Mail";
   else if(weight<=10) return "Regular";
    else return "Heavy";
  };
  const handleApprove =async (id)=>{
    try{
      const response =await fetch(
       ` http://127.0.0.1:8000/apply-insurance/${id}`,
       {
        method:"POST",
       }
      );
      if(!response.ok){
        throw new Error("Failed to approve insurance");
      }
      const updateCustomer=await response.json();
      setTaable((prev)=>
        prev.map((item)=>
          item.Id === id?{
            ...item,
            Insurance:updateCustomer.Insurance,
           Approval_status:updateCustomer.Approval_status,
          }:item
        )
      );
    }
    catch(error){
      console.log(error);
    }
  };
  return (
    <>
      <h3 className="hello2 mt-4 text-center">Customer Table</h3>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>Name</th>
            <th>Street</th>
            <th>House No.</th>
            <th>P.Code</th>
            <th>City</th>
            <th>Weight</th>
            <th>Value</th> 
            <th>Department</th> 
            <th>Insurance</th>
            <th>Approval Status</th>
          </tr>
        </thead>
        <tbody>
          {Array.isArray(taable) &&
            taable.map((item) => (
              <tr key={item.Id}>
                <td>{item.Name}</td>
                <td>{item.Street}</td>
                <td>{item.HouseNumber}</td>
                <td>{item.PostCode}</td>
                <td>{item.City}</td>
                <td>{item.Weight}</td>
                <td>{item.Value}</td>
                <td>{getDepartment(Number(item.Weight))}</td>
                <td>{item.Value>1000 && item.Insurance!=="Completed"?(<button className="btn btn-sm btn-success " onClick={()=> handleApprove(item.Id)}>Approve Insurance</button>):(item.Insurance || "NO need")}</td>
                <td>{item.Approval_status}</td>
              </tr> ))}
        </tbody>
      </table>
    </>
  );
}

 
