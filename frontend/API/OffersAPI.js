import API from "./API";
const prefix = "/offer";

const create = (building_ids) => {
  return API.post(`${prefix}/`, {
    "building_ids": building_ids
  });
};

const getById = (offer_id) => {
  return API.get(`${prefix}/${offer_id}`);
};

export default {
  create,
  getById,
};
