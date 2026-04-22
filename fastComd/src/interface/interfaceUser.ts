export interface InHero {
    id: number,
    name: string,
    age?: number,
    secret_name: string,
    hero?: InHero
}

export interface InGetHero {
    offset: number;
    limit: number;
}


export interface InImgCode{
    id:string,
    img_url:string,
}