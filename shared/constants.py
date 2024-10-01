standard_values = {
    "md_insert_user": "adf-user",
    "md_update_user": "adf-user",
    "md_dq_error_indicator": "NE",
    "certified_flag": ["N", "Y"],
    "certified_standard": ["RMS","RCS/GRS","RWS","RDS","NA","RAS","OCS"],
    "md_source_system_identifier" : ["CB-EST", "CB-ICA", "CB-USB", "CB-ETK", "CB-CUC", "CB-GSI", "CB-IDF", "OCS - ICEA - 05", "CB-ULV", "CB-CUI", "GRS - ICEA - 05", "RCS - ICEA - 05", "CB-GCL", "RDS - ICEA - 05", "CB-OIA", "CB-IFC", "CB-EGL", "CB-CPB", "CB-SGC", "CB-CGI", "CB-KEK", "CB-CUT"],
    "material_type": ["contentclaimed", "In-conversion", "Non-Certified", "Organic", "Recycled pre/post-consumer", "Recycledpost_consumer", "Recycledpre-consumer", "Responsible_RAS", "Responsible_RDS", "Responsible_RMS", "Responsible_RWS", "Sustainably sourced"],
    "usda_compliant_flag": ["N", "Y"],
    "usda_nop_compliant_flag": ["N", "Y"],
    "input_usda_non_compliant_flag": ["N", "Y"],
    "tc_status": ["W", "V", "I", "A"],
    "selling_on_behalf_of_flag": ["N", "Y"],
    "buying_on_behalf_of_flag": ["N", "Y"]
}

sql_table_structures = {

    "input_tc_component_raw_material" : {
        "input_component_raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_tc_component_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "input_tc_component_raw_material_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "input_tc_component_raw_material_percentage": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_flag": {
            "datatype": "nchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_standard": {
            "datatype": "nvarchar(10)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "input_tc_component_standard" : {
        "input_tc_component_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_tc_component_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "input_tc_component_certified_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_certified_weight_used": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "input_tc_component": {
        "input_tc_component_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_product_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "input_tc_product_component_no": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_detail": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_trims_excluded": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_associated_tc": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_fiber_length": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_yarn_count": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_fabric_weight_and_construct": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_fabric_weight_of_finished_product": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_net_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_supplementary_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_component_info_additional": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "input_tc_product_standard": {
        "input_tc_product_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_product_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "input_product_standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "input_product_certified_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_product_certified_weight_used": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "org_facility_process": {
        "process_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "process_category_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "facility_certified_subcontractor_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "process_user_specific_term": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "process_category_user_specific_term": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "is_derived_from_mf_or_fa_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "org_facility_standard": {
        "facility_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "facility_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "org_facility": {
        "facility_certified_subcontractor_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "facility_number": {
            "datatype": "varchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_subcontractor_license_number": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "facility_te_id": {
            "datatype": "varchar(20)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "oar_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "address_1": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "address_2": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "address_3": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "postcode": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "town": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "state_or_province_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "country_or_area_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "independently_certified_contractor_start_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "independently_certified_contractor_end_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "independently_certified_contractor_certification_body_name": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "scope_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "last_audit_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "facility_type_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "is_derived_from_mf_or_fa_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "facility_te_id_sf_account_license_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "facility_sf_account_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        }
    },

    "org_product_product_details_category": {
        "ppd_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_cat_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_detail_cat_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "facility_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_category_user_specific_term": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_detail_user_specific_term": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_product_no": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "is_derived_from_mf_or_fa_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },
    
    "org_raw_materials": {
        "rm_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_product_details_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "raw_materials_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "percentage_or_percentage_range": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "is_derived_from_mf_or_fa_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },
    
    "org_sc_product_standard_label_grade": {
        "org_sc_product_standard_label_grade_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "ppd_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "is_derived_from_mf_or_fa_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },
    
    "ref_code": {
        "code_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "code_1": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_type_1": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "description_1": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_2": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_type_2": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_description_2": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_3": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_type_3": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "code_description_3": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "status": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },
    
    "ref_material_content_standard_material_types": {
        "smt_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "standard": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "material_type": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },
    
    "ref_material_content_standard_raw_material_type": {
        "sm_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "material_code": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "material_type_identifier": {
            "datatype": "int",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "material_name": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "sc_component_raw_material": {
        "sc_component_raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "sc_product_component_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_component_raw_material_code_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_component_raw_material_percentage": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "sc_component_standard_label_grade": {
        "sc_component_standard_label_grade_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "sc_product_component_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_component_standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "sc_product_component": {
        "sc_product_component_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "ppd_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "sc_product_component_no": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_component_detail": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "sc_scope_certificate": {
        "scope_certificate_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "scope_certificate_number": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "issue_on": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "valid_to": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "anniversary_date": {
            "datatype": "nvarchar(5)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_last_updated_date": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "date_of_issue": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_status": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "place_of_issue": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_no_logically_updated": {
            "datatype": "int",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "version_number": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_legacy_no": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "gots_scope_certificate_number": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "license_code": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "accrediation_body_number": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "accrediation_body_name": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "standard_body_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "certification_body_name": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "standard_body_name": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_original_no": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_file_load_sk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_cb_scope_stipulation_set_text": {
            "datatype": "nvarchar(2000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "is_HIST_ind": {
            "datatype": "bit",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "batch_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "cb_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "cb_first_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_withdrawl_reason_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_suspension_reason_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "sc_extended_until": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_last_audit_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_last_audit_start": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_transfer_audit_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "sc_standard": {
        "s_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "start_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "version_number": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "farm_number": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "audit_calendar_day_number": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "sc_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "claims_approved": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "end_date": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "program": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_certified_raw_material_country_state": {
        "certified_raw_material_country_state_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "certified_raw_material_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "certified_raw_material_country_or_area_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "certified_raw_material_state_or_province_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_certified_raw_material": {
        "certified_raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "certified_raw_material_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "certified_raw_material_weight": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_raw_material_country_or_area": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_raw_material_state_or_province": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_component_raw_material": {
        "tc_component_raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "tc_component_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "tc_component_raw_material_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "tc_component_raw_material_percentage": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_flag": {
            "datatype": "nchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_standard": {
            "datatype": "nvarchar(10)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_component_standard": {
        "tc_component_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "tc_component_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "tc_component_standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "tc_component_certified_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_component": {
        "tc_component_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "tc_product_component_no": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_detail": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_trims_excluded": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_associated_tc": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_fiber_length": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_yarn_count": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_fabric_weight_and_construct": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_fabric_weight_of_finished_product": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_net_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_supplementary_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_component_info_additional": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_input_certified_weight": {
        "tc_input_certified_weight_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "tc_input_transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "tc_input_certified_weight_used": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_input_farm_trader_organic": {
        "input_farm_trader_organic_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "input_trader_transaction_certificate": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_farm_transaction_certificate": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_farm_sc_no": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_organic_farming_standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_input_product": {
        "input_product_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "usda_compliant_flag": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "article_number": {
            "datatype": "nvarchar(2000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "number_of_units_in_shipment": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "production_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_category_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_detail_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "trims_excluded": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fiber_length": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "yarn_count": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fabric_weight_and_construct": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fabric_weight_of_finished_product": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "associated_transaction_certificate_number": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_category_user_specific_term": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_detail_user_specific_term": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_product_units_metric": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_product_info_additional": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_input_raw_material": {
        "input_raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_raw_material_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "input_product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "raw_material_percentage": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "varchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_weight": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_flag": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_weight_used": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_standard": {
            "datatype": "nvarchar(10)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_input_transaction_certificate": {
        "input_transation_certificate_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "input_transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "seller_license_number": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "scope_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "input_usda_non_compliant_flag": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_cb_licensing_code": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "transaction_certificate_number": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "output_product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "input_seller_sc_no": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_tc_seller_te_id": {
            "datatype": "nvarchar(15)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_non_certified_trader_name": {
        "non_certified_trader_name_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "tc_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "non_certified_trader_name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_non_certified_trader_te_id": {
            "datatype": "nvarchar(15)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_organic_farming_standard": {
        "tc_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "organic_farming_standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "ofs_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        }
    },

    "tc_product_purchase_order_no": {
        "purchase_order_no_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "purchase_order_number": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_product_shipment_no": {
        "tc_product_shipment_no_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_shipment_no": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(50)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_product_standard": {
        "product_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_standard_label_grade_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_certified_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_product": {
        "product_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "product_identifier": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "production_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "shipment_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "article_number": {
            "datatype": "nvarchar(2000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "number_of_units": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "net_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "supplementary_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_category_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_detail_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "trims_excluded": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fiber_length": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "yarn_count": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fabric_weight_contruction": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "last_processor_name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "last_processor_license_number": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "last_processor_country": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "component_product_flag": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_category_user_specific_term": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_detail_user_specific_term": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "product_additional_associated_transaction_certificate": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "units_metric": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "fabric_weight_of_finished_product": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_product_last_processor_te_id": {
            "datatype": "nvarchar(15)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_product_info_additional": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_raw_material": {
        "raw_material_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "raw_material_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "product_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "raw_material_percentage": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_weight": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_flag": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "certified_standard": {
            "datatype": "nvarchar(10)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "waste_percentage": {
            "datatype": "decimal(20, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_shipment_invoice": {
        "tc_shipment_invoice_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "shipment_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "invoice_number": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_shipment": {
        "shipment_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "shipment_identifier": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "shipment_date": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "consignee": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "shipment_document_number": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "gross_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_address_1": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_address_2": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_address_3": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_postcode": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_town": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_state_or_province_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "consignee_country_or_area_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "consignee_te_id": {
            "datatype": "nvarchar(15)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_standard": {
        "tc_standard_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "tc_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "standard_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "certified_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_transaction_certifcate": {
        "transaction_certifcate_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "transaction_certificate_number": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "date_of_issue": {
            "datatype": "date",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "gross_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "net_shipping_weight": {
            "datatype": "decimal(13, 2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "tc_status": {
            "datatype": "nvarchar(1)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "place_of_issue": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "version_statement": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_license_number": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_address_1": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_address_2": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_address_3": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_postcode": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_town": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_country_or_area_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "seller_declarations": {
            "datatype": "nvarchar(2000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_license_number": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_name": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_address_1": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_address_2": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_address_3": {
            "datatype": "nvarchar(1000)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_postcode": {
            "datatype": "nvarchar(40)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_town": {
            "datatype": "nvarchar(255)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "buyer_state_or_province_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "buyer_country_or_area_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tc_transaction_certificate_seller": {
        "transaction_certificate_seller_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "seller_sc_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "transaction_certificate_fk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": False,
            "is_fk": True
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "seller_sc_no": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    },

    "tr_transaction_certificate_traceability": {
        "traceability_sk": {
            "datatype": "bigint",
            "is_null": False,
            "is_identity": True,
            "is_fk": False
        },
        "traceability_id": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "traceability_sequence_id": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "output_fk": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": True
        },
        "md_insert_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_datetime": {
            "datatype": "datetime",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_insert_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_update_user": {
            "datatype": "nvarchar(max)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_dq_error_indicator": {
            "datatype": "varchar(2)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_source_system_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "md_process_identifier": {
            "datatype": "nvarchar(100)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "chain_id": {
            "datatype": "bigint",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "output_transaction_certificate_number": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        },
        "input_transaction_certificate_number": {
            "datatype": "nvarchar(200)",
            "is_null": True,
            "is_identity": False,
            "is_fk": False
        }
    }
}
