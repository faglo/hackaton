import axios from "axios";

export default axios.create({
  baseURL: 'http://92.63.105.59/',
  responseType: "json",
});
