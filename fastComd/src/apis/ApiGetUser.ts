import axios from "axios"
import type {InHero, InGetHero, InImgCode} from "../interface/interfaceUser.ts";

export const BaseUrl: string = "http://127.0.0.1:8000"

export async function ApigetUser(params?: InGetHero): Promise<InHero[]> {
    const res = await axios.get(`${BaseUrl}/api_v1/heroes/`, {
        params: params
    })

    return res.data
}

export async function getCode(): Promise<InImgCode> {
    const res = await axios.get(`${BaseUrl}/api_create_yzm/create_yzm`, {})
        console.log("getCode res", res.data)
    const Data:InImgCode = {
        "id":res.data.id,
        "img_url":BaseUrl+'/'+ res.data.img_url
    }
    console.log("getCode data", Data)
    return Data
}