import API from "./API";
const prefix = "/buildings";

const prefix = '/building'
const getByFilter = (
  residential_complex,
  building,
  area_from,
  area_to,
  rooms,
  floor_from,
  floor_to,
  price_from,
  price_to
) => {
  return API.get(
    `${prefix}/?residential_complex=${residential_complex}&building=${building}&area_from=${area_from}&area_to=${area_to}&rooms=${rooms}&floor_from=${floor_from}&floor_to=${floor_to}&price_from=${price_from}&price_to=${price_to}`
  );
};

const getFilterProperties = () => {
  return API.get(`${prefix}/filters`);
};


export default {
  getByFilter,
  getFilterProperties,
};
