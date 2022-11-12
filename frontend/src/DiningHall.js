import React from 'react'

function DiningHall(props) {
    return (
        <div className='diningHall' onClick={() => {console.log(props.name)}}
            style={{
                display: 'flex'
            }}
        >
            <img 
                src={require("./" + props.name + ".jpg")} 
                alt="not found"
                style={{
                    height: '90vh',
                    margin: 'auto'
                }}  
            />
        </div>
    );
}

export default DiningHall;