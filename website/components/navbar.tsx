import Image from "next/image"

function Navbar() {
    return (
        <div className="flex min-h-min flex-row justify-between items-center p-9">
            <div className="inline-flex items-center m-3">
                <a href="/">
                <Image src="/LightJort.svg" height={90} width={90} alt="Shifty Tech Logo" />
                </a>
                <a href="/">
                <h1 className="pl-9 font-han text-5xl">
                    Shifty Tech
                </h1>
                </a>
            </div>
            <div className="flex flex-row justify-between items-center m-3">
                <a href="/install">
                <h2 className="font-lato text-2xl pr-9">
                    Install
                </h2>
                </a>
                <a href="/guide">
                <h2 className="font-lato text-2xl pr-9">
                Guide
                </h2>
                </a>
                <a className="pr-9" href="https://devpost.com/software/shiftytech" rel="noopener noreferrer" aria-label="Shifty Tech DevPost">
                <Image src="/devpost-icon.svg" height={50} width={50} alt="Devpost Logo" />
                </a>
                <a href="https://github.com/ShiftyTech" rel="noopener noreferrer" aria-label="Shifty Tech Github">
                <Image src="/github-mark-white.svg" height={50} width={50} alt="Github Logo" />
                </a>
            </div>
     </div>
    )
}

export default Navbar;