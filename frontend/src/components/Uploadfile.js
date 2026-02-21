import {useState,useEffect} from "react";
import Taable from "./Taable";
export default function Uploadfile(){
 const [file,setFile]=useState(null);
  const [taable, setTaable] = useState([]);
  const fetchTaable=async()=>{
    try{
      const res = await fetch("http://127.0.0.1:8000/responsefile");
      if (!res.ok) {
    throw new Error("Network response was not ok");
  }
      const data = await res.json();
      // Take the response from backend and convert it into JavaScript object. so that readable”
      console.log("DATA:", data);
      setTaable(data);
    } catch(err){
      console.error(err);
    }
  };
  useEffect(() => {
  fetchTaable();
}, []);
// fetchTaable();
    const handleFileChange=(e)=>{
      setFile(e.target.files[0]);
    }
    const handleSubmit=async(e)=>{
      e.preventDefault(); //prevent page load
    if(!file){
      alert("please select a file");
      return;
    }
    const formData=new FormData();
    formData.append("file",file);
    try{
      const response=await fetch("http://127.0.0.1:8000/uploadfile/",{
        method:"POST",
        body:formData,
  });
      if (!response.ok) {
  throw new Error("Network response was not ok");
}
const data = await response.json();
      console.log(data);
      alert( "Table created successfully");
   fetchTaable();
  } catch (error) {
    console.error("Upload failed:", error);
    alert("Error uploading file");
  }
    } 
  return (
    <div className="hello container py-5">
       <div className="row justify-content-center">
      <div className="col-md-5">
  <div className="card shadow p-4" style={{width: "400px"}}>
    <h3 className="mb-4 text-center">Upload XML File</h3>
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
      <h6>  <label className="form-label">Choose file to parse</label></h6>
        <input 
          type="file" 
          className="form-control"
        onChange={handleFileChange} />
      </div>
      <div className="text-center">
        <button type="submit" className="btn btn-primary px-4">
          Submit
        </button>
      </div>
    </form>
    </div>
    </div> 
    </div> 
    {/* Table BELOW card */}
    {taable.length > 0 && (
      <div className="mt-5 mx-5">
        <Taable taable={taable} setTaable={setTaable} />
      </div>
    )}
  </div>
);
}
